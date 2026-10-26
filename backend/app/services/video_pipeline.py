"""Video validation + frame extraction. Real OpenCV; deterministic and capped."""
from __future__ import annotations

from pathlib import Path

import cv2

from app.core.config import get_settings
from app.core.logging import get_logger

log = get_logger("video")

ALLOWED_EXTS = {".mp4", ".mov", ".avi", ".mkv", ".webm"}


def validate_video(path: Path, size_bytes: int) -> tuple[bool, str, float | None]:
    s = get_settings()
    if path.suffix.lower() not in ALLOWED_EXTS:
        return False, f"Unsupported container {path.suffix}; allowed: {sorted(ALLOWED_EXTS)}", None
    if size_bytes > s.MAX_UPLOAD_MB * 1024 * 1024:
        return False, f"File exceeds {s.MAX_UPLOAD_MB} MB cap", None
    cap = cv2.VideoCapture(str(path))
    if not cap.isOpened():
        return False, "Undecodable video stream", None
    fps = cap.get(cv2.CAP_PROP_FPS) or 25.0
    frames = cap.get(cv2.CAP_PROP_FRAME_COUNT) or 0
    cap.release()
    duration = float(frames / fps) if fps else None
    if duration is not None and duration < 1.0:
        return False, "Video too short (<1s)", duration
    return True, "ok", duration


def extract_frames(video_path: Path, out_dir: Path) -> tuple[int, float, float]:
    """Sample FRAME_SAMPLE_COUNT evenly-spaced frames → out_dir/frame_XXXX.jpg.

    Deterministic: fixed stride from frame 0, no randomness, no full-video buffering.
    Returns (frames_written, frame_width_px, frame_height_px). Dims are (0, 0)
    only when no frame could be decoded.
    """
    s = get_settings()
    out_dir.mkdir(parents=True, exist_ok=True)
    cap = cv2.VideoCapture(str(video_path))
    total = int(cap.get(cv2.CAP_PROP_FRAME_COUNT) or 0)
    want = max(1, min(s.FRAME_SAMPLE_COUNT, total or s.FRAME_SAMPLE_COUNT))
    step = max(1, total // want) if total else 1
    idx, taken = 0, 0
    width, height = 0.0, 0.0
    while taken < want:
        cap.set(cv2.CAP_PROP_POS_FRAMES, idx)
        ok, frame = cap.read()
        if not ok or frame is None:
            break
        if taken == 0:
            height, width = float(frame.shape[0]), float(frame.shape[1])
        cv2.imwrite(str(out_dir / f"frame_{taken:04d}.jpg"), frame)
        taken += 1
        idx += step
    cap.release()
    log.info("extracted=%d total=%d dims=%sx%s", taken, total, width, height)
    return taken, width, height
