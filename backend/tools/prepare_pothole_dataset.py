"""Prepare the public pothole dataset (jaygala24/pothole-detection) for YOLO26-Seg.

Boxes are converted to 4-corner polygons so segmentation training works from
box-only annotations. Writes YOLO-seg layout + data.yaml.
"""
from __future__ import annotations

import random
import shutil
from pathlib import Path

RAW = Path(r"C:\Users\jeeva\AppData\Local\Temp\opencode\ds\raw\Pothole Dataset")
OUT = Path(r"C:\Users\jeeva\AppData\Local\Temp\opencode\ds\yolo")
VAL_FRACTION = 0.15
SEED = 42


def box_to_polygon(line: str) -> str:
    cls, cx, cy, w, h = line.split()
    x0 = float(cx) - float(w) / 2
    y0 = float(cy) - float(h) / 2
    x1 = float(cx) + float(w) / 2
    y1 = float(cy) + float(h) / 2
    pts = [f"{v:.6f}" for v in (x0, y0, x1, y0, x1, y1, x0, y1)]
    return f"{cls} " + " ".join(pts)


def main() -> None:
    if OUT.exists():
        shutil.rmtree(OUT)
    for split in ("train", "val"):
        (OUT / "images" / split).mkdir(parents=True)
        (OUT / "labels" / split).mkdir(parents=True)

    images = sorted(RAW.glob("*.jpg"))
    random.Random(SEED).shuffle(images)
    n_val = max(1, round(len(images) * VAL_FRACTION))
    val_set = set(images[:n_val])

    for img in images:
        split = "val" if img in val_set else "train"
        shutil.copy2(img, OUT / "images" / split / img.name)
        label = img.with_suffix(".txt")
        if label.exists():
            lines = [box_to_polygon(ln) for ln in label.read_text().splitlines() if ln.strip()]
            (OUT / "labels" / split / f"{img.stem}.txt").write_text("\n".join(lines) + "\n")

    (OUT / "data.yaml").write_text(
        "train: {}/images/train\n"
        "val: {}/images/val\n"
        "names:\n"
        "  0: pothole\n".format(OUT, OUT)
    )
    print(f"train={len(images) - n_val} val={n_val} -> {OUT}")


if __name__ == "__main__":
    main()
