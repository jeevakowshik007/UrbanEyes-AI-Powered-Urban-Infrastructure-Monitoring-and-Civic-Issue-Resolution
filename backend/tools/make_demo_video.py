"""Generate a synthetic street-drive demo video for UrbanEyes.

Renders a procedural first-person drive (sky, buildings, road, lane dashes,
traffic) and composites real pothole-photo patches (from the prepared dataset,
with their ground-truth boxes) onto the road plane so the fine-tuned YOLO26-Seg
model has genuine damage texture to detect.

Usage: python tools/make_demo_video.py [out_path] [seconds]
"""
from __future__ import annotations

import random
import sys
from pathlib import Path

import cv2
import numpy as np

DS = Path(r"C:\Users\jeeva\AppData\Local\Temp\opencode\ds\raw\Pothole Dataset")
W, H, FPS = 1280, 720, 30
HORIZON = int(H * 0.40)


def load_pothole_crops(n: int = 10, seed: int = 7) -> list[np.ndarray]:
    rng = random.Random(seed)
    labels = sorted(DS.glob("*.txt"))
    rng.shuffle(labels)
    crops: list[np.ndarray] = []
    for lbl in labels:
        if len(crops) >= n:
            break
        img_path = lbl.with_suffix(".jpg")
        img = cv2.imread(str(img_path))
        if img is None:
            continue
        ih, iw = img.shape[:2]
        for line in lbl.read_text().splitlines():
            parts = line.split()
            if len(parts) != 5:
                continue
            _, cx, cy, bw, bh = map(float, parts)
            x0 = int(max(0, (cx - bw / 2) * iw))
            y0 = int(max(0, (cy - bh / 2) * ih))
            x1 = int(min(iw, (cx + bw / 2) * iw))
            y1 = int(min(ih, (cy + bh / 2) * ih))
            if x1 - x0 < 40 or y1 - y0 < 40:
                continue
            pad_x, pad_y = int((x1 - x0) * 0.25), int((y1 - y0) * 0.25)
            x0, y0 = max(0, x0 - pad_x), max(0, y0 - pad_y)
            x1, y1 = min(iw, x1 + pad_x), min(ih, y1 + pad_y)
            crops.append(img[y0:y1, x0:x1])
            break
    return crops


def depth_y(t: float) -> int:
    """Screen y for depth t in [0 far .. 1 near]."""
    return int(HORIZON + (H - HORIZON) * (t ** 1.6))


def road_half_w(t: float) -> int:
    top, bot = int(W * 0.045), int(W * 0.52)
    return int(top + (bot - top) * (t ** 1.6))


def feathered_patch(patch: np.ndarray, width: int, height: int) -> tuple[np.ndarray, np.ndarray]:
    p = cv2.resize(patch, (max(8, width), max(6, height)), interpolation=cv2.INTER_AREA)
    mask = np.zeros((p.shape[0], p.shape[1]), np.uint8)
    cv2.ellipse(mask, (p.shape[1] // 2, p.shape[0] // 2),
                (p.shape[1] // 2 - 1, p.shape[0] // 2 - 1), 0, 0, 360, 255, -1)
    mask = cv2.GaussianBlur(mask, (0, 0), sigmaX=max(3, p.shape[1] // 14))
    return p, mask


def paste(frame: np.ndarray, patch: np.ndarray, mask: np.ndarray, cx: int, cy: int) -> None:
    h, w = patch.shape[:2]
    x0, y0 = cx - w // 2, cy - h // 2
    x1, y1 = x0 + w, y0 + h
    sx0, sy0 = max(0, -x0), max(0, -y0)
    x0, y0, x1, y1 = max(0, x0), max(0, y0), min(W, x1), min(H, y1)
    if x1 <= x0 or y1 <= y0:
        return
    p = patch[sy0:sy0 + (y1 - y0), sx0:sx0 + (x1 - x0)]
    m = (mask[sy0:sy0 + (y1 - y0), sx0:sx0 + (x1 - x0)].astype(np.float32) / 255.0)[..., None]
    roi = frame[y0:y1, x0:x1].astype(np.float32)
    frame[y0:y1, x0:x1] = (p * m + roi * (1 - m)).astype(np.uint8)


def make_scene() -> np.ndarray:
    frame = np.zeros((H, W, 3), np.uint8)
    for y in range(HORIZON):
        f = y / max(1, HORIZON)
        frame[y, :] = (int(240 - 60 * f), int(210 - 30 * f), int(150 + 60 * f))
    rng = random.Random(3)
    x = 0
    while x < W:
        bw = rng.randint(60, 140)
        bh = rng.randint(50, 150)
        col = (rng.randint(70, 120), rng.randint(75, 125), rng.randint(90, 140))
        frame[HORIZON - bh:HORIZON, x:x + bw] = col
        for wy in range(HORIZON - bh + 8, HORIZON - 8, 22):
            for wx in range(x + 8, x + bw - 10, 20):
                if rng.random() < 0.55:
                    frame[wy:wy + 10, wx:wx + 10] = (210, 225, 235)
        x += bw + rng.randint(4, 26)
    road = np.zeros((H, W), np.uint8)
    cv2.fillPoly(road, [np.array([
        [W // 2 - 58, HORIZON], [W // 2 + 58, HORIZON], [W - 40, H], [40, H]
    ], np.int32)], 255)
    noise = rng.randint(40, 60)
    asphalt = np.full((H, W, 3), noise, np.uint8)
    grain = (np.random.default_rng(1).normal(0, 9, (H, W, 1))).astype(np.int16)
    asphalt = np.clip(asphalt.astype(np.int16) + grain, 0, 255).astype(np.uint8)
    frame[road > 0] = asphalt[road > 0]
    side = np.full((H, W, 3), 130, np.uint8)
    side_mask = ((road == 0) & (np.arange(H)[:, None] >= HORIZON)).astype(bool)
    frame[(np.arange(H)[:, None] >= HORIZON) & (road == 0)] = \
        side[(np.arange(H)[:, None] >= HORIZON) & (road == 0)]
    cv2.rectangle(frame, (0, HORIZON - 6), (W, HORIZON + 6), (120, 150, 110), -1)
    return frame


def draw_dashes(frame: np.ndarray, phase: float) -> None:
    for k in range(-2, 14):
        t = ((k + phase) / 12.0)
        if t <= 0.02 or t >= 1.0:
            continue
        y = depth_y(t)
        hw = max(2, int(6 + 26 * t))
        hh = max(3, int(8 + 42 * t))
        x = W // 2
        if k % 2 == 0:
            cv2.rectangle(frame, (x - hw // 2, y - hh), (x + hw // 2, y), (235, 235, 235), -1)


def draw_car(frame: np.ndarray, t: float, lane: int, color: tuple[int, int, int]) -> None:
    if t <= 0.03 or t >= 1.0:
        return
    y = depth_y(t)
    cw = int(60 + 260 * t)
    ch = int(45 + 150 * t)
    x = W // 2 + lane * road_half_w(t) * 0.55
    x0, y0 = int(x - cw / 2), int(y - ch)
    if x0 < -cw or x0 + cw > W + cw:
        return
    cv2.rectangle(frame, (x0, y0), (x0 + cw, y0 + ch), color, -1)
    cv2.rectangle(frame, (x0 + int(cw * 0.18), y0 + int(ch * 0.08)),
                  (x0 + int(cw * 0.82), y0 + int(ch * 0.5)), (185, 200, 215), -1)
    cv2.rectangle(frame, (x0, y0 + ch - max(3, int(ch * 0.2))),
                  (x0 + cw, y0 + ch), (30, 30, 35), -1)


def main() -> None:
    out = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("demo/street_drive_demo.mp4")
    seconds = int(sys.argv[2]) if len(sys.argv) > 2 else 18
    out.parent.mkdir(parents=True, exist_ok=True)
    crops = load_pothole_crops()
    if not crops:
        raise SystemExit("no pothole crops found — run tools/prepare_pothole_dataset.py first")
    scene = make_scene()
    total = seconds * FPS
    vw = cv2.VideoWriter(str(out), cv2.VideoWriter_fourcc(*"mp4v"), FPS, (W, H))
    rng = random.Random(11)

    events = []  # (start_frame, duration, lane, crop)
    f = 0
    idx = 0
    while f < total:
        if not events or f >= events[-1][0] + 40:
            events.append((f + rng.randint(0, 30), rng.randint(110, 150),
                           rng.choice([-1, 0, 0, 1]), crops[idx % len(crops)]))
            idx += 1
        cars = [
            (int(total * 0.10), 170, -1, (60, 70, 160)),
            (int(total * 0.38), 170, 1, (50, 130, 70)),
            (int(total * 0.66), 170, -1, (170, 90, 60)),
        ]
        frame = scene.copy()
        jitter = rng.randint(-2, 2)
        frame = np.roll(frame, jitter, axis=0)
        draw_dashes(frame, (f * 0.045) % 1.0)
        for cs, cd, lane, col in cars:
            t = (f - cs) / cd
            if 0 < t < 1:
                draw_car(frame, t, lane, col)
        for (sf, dur, lane, crop) in events:
            if sf <= f < sf + dur:
                t = (f - sf) / dur
                y = depth_y(t)
                half = road_half_w(t)
                cx = int(W // 2 + lane * half * 0.5 + rng.randint(-6, 6))
                pw = int(60 + 420 * (t ** 1.5))
                ph = max(10, int(pw * 0.38 * (0.55 + 0.45 * t)))
                patch, mask = feathered_patch(crop, pw, ph)
                paste(frame, patch, mask, cx, y)
        frame = np.clip(frame.astype(np.int16) + int(4 * np.sin(f / 17)), 0, 255).astype(np.uint8)
        vw.write(frame)
        f += 1
    vw.release()
    print(f"wrote {out} frames={total} duration={seconds}s pothole_crops={len(crops)}")


if __name__ == "__main__":
    main()
