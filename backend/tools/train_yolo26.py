"""Fine-tune YOLO26-Seg (nano) on the prepared pothole dataset — CPU friendly.

Usage: python tools/train_yolo26.py [epochs]
Prints the resulting best.pt path when finished.
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

from ultralytics import YOLO

DATA = Path(r"C:\Users\jeeva\AppData\Local\Temp\opencode\ds\yolo\data.yaml")
WEIGHTS = Path(__file__).resolve().parents[1] / "weights" / "yolo26n-seg.pt"
# Outside OneDrive: syncing checkpoints mid-training starves the dataloader.
PROJECT = Path(r"C:\Users\jeeva\AppData\Local\Temp\opencode\runs\street-damage")


def main() -> None:
    epochs = int(sys.argv[1]) if len(sys.argv) > 1 else 35
    started = time.time()
    model = YOLO(str(WEIGHTS))
    results = model.train(
        data=str(DATA),
        epochs=epochs,
        imgsz=416,
        batch=16,
        device="cpu",
        workers=8,
        patience=12,
        project=str(PROJECT),
        name="pothole-finetune",
        exist_ok=True,
        verbose=True,
    )
    best = Path(results.save_dir) / "weights" / "best.pt"
    mins = (time.time() - started) / 60
    print(f"TRAINING_DONE minutes={mins:.1f} best={best}")


if __name__ == "__main__":
    main()
