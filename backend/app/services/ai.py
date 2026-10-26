"""Computer-vision layer: YOLO26-Seg evidence providers + deterministic severity.

YOLO26-Seg  → detection/segmentation evidence (boxes, masks, confidence, category).
Reasoning   → handled by the Local Urban Infrastructure Reasoning Engine
               (`app/services/reasoning.py`); this module only aggregates evidence.

DevHeuristicAdapter is CLEARLY isolated dev-only fallback (CV_PROVIDER=mock).
Real inference needs ultralytics==8.4.142 (tested, ships yolo26-seg.yaml) plus a
trained checkpoint at YOLO26_SEG_WEIGHTS — neither is bundled with this repo.
"""
from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass, field
from pathlib import Path

from app.core.config import get_settings
from app.core.logging import get_logger
from app.schemas import Severity

log = get_logger("ai")

# Supported infrastructure severity categories (extensible — add here + CATEGORY_IMPACT /
# recommendation templates in reasoning.py; pipeline and UI adapt automatically).
CATEGORIES = ("road_condition", "waste_management", "drainage", "street_infrastructure")

# Detections whose label is not in the application vocabulary. They are kept for
# auditability but EXCLUDED from severity scoring — never silently relabeled.
UNMAPPED_CATEGORY = "unmapped"

# Application class → category vocabulary. These are OUR mappings, NOT guaranteed
# model classes: the real checkpoint's model.names is authoritative (see map_class).
CLASS_TO_CATEGORY: dict[str, str] = {
    "pothole": "road_condition", "crack": "road_condition", "road_damage": "road_condition",
    "garbage": "waste_management", "litter": "waste_management", "dumping": "waste_management",
    "drain": "drainage", "waterlog": "drainage", "clogged_drain": "drainage",
    "pole": "street_infrastructure", "sign": "street_infrastructure",
    "streetlight": "street_infrastructure", "sidewalk": "street_infrastructure",
}

# Per-class severity PRIOR (informational only). The model provides visual evidence;
# FINAL severity always comes from the LocalReasoningEngine's evidence factors.
# This prior only seeds per-finding counts and never overrides reasoning.
CLASS_SEVERITY_PRIOR: dict[str, Severity] = {
    "pothole": "critical", "road_damage": "critical", "dumping": "critical",
    "waterlog": "critical", "crack": "medium", "garbage": "medium",
    "clogged_drain": "medium", "drain": "weak", "litter": "weak",
    "pole": "weak", "sign": "weak", "streetlight": "medium", "sidewalk": "medium",
}

# Mock frames pretend to be VGA so the reasoning path is exercised realistically.
MOCK_FRAME_WIDTH = 640.0
MOCK_FRAME_HEIGHT = 480.0

# Segmentation polygons are downsampled to at most this many points per detection
# (keeps stored evidence compact — never raw mask tensors in the database).
MAX_POLYGON_POINTS = 32


def normalize_label(name: object) -> str:
    """Lowercase, spaces→underscores, strip anything outside [a-z0-9_]."""
    text = str(name or "").strip().lower().replace(" ", "_")
    return re.sub(r"[^a-z0-9_]+", "", text).strip("_")


def map_class(label: str) -> str | None:
    """Application category for a model label, or None when the checkpoint's
    vocabulary does not contain it (caller must treat None as unmapped)."""
    return CLASS_TO_CATEGORY.get(normalize_label(label))


@dataclass
class CVDetection:
    label: str
    category: str
    severity: Severity
    confidence: float
    bbox: tuple[float, float, float, float] = (0, 0, 0, 0)
    frame_index: int = 0
    frame_width: float = 0.0   # actual extracted-frame width in px (0 = unknown)
    frame_height: float = 0.0  # actual extracted-frame height in px (0 = unknown)
    mask_polygon: list = field(default_factory=list)  # normalized [[x,y],...] ≤32 pts
    mask_area: float | None = None  # polygon area as frame fraction (None = no mask)


@dataclass
class CVEvidence:
    detections: list[CVDetection] = field(default_factory=list)
    frames_analyzed: int = 0
    provider: str = "mock"
    has_masks: bool = False  # True when at least one detection carried a real mask

    def summary(self) -> dict:
        counts: dict[str, int] = {"weak": 0, "medium": 0, "critical": 0}
        cats: dict[str, dict[str, int]] = {}
        for d in self.detections:
            if d.category == UNMAPPED_CATEGORY:
                continue
            counts[d.severity] += 1
            cats.setdefault(d.category, {}).setdefault(d.severity, 0)
            cats[d.category][d.severity] += 1
        return {"counts": counts, "by_category": cats, "frames": self.frames_analyzed}


class SegmentationProvider:
    name = "base"

    def infer_frames(self, frames_dir: str, count: int) -> CVEvidence:  # pragma: no cover
        raise NotImplementedError


class DevHeuristicAdapter(SegmentationProvider):
    """Deterministic dev-only stand-in. Uses file hash → stable pseudo-detections.
    NEVER used when CV_PROVIDER=yolo. Labeled provider='mock' in every response."""
    name = "mock"

    LABELS = tuple(CLASS_TO_CATEGORY)

    def infer_frames(self, frames_dir: str, count: int) -> CVEvidence:
        seed = int(hashlib.sha256(frames_dir.encode()).hexdigest(), 16)
        dets: list[CVDetection] = []
        for i in range(max(1, count)):
            label = self.LABELS[(seed >> (i * 5)) % len(self.LABELS)]
            # Map hash bits to a confidence in [0.4, 0.95]
            conf = 0.4 + ((seed >> (i * 3)) % 55) / 100.0
            if conf < 0.35:
                continue
            dets.append(CVDetection(
                label=label, category=CLASS_TO_CATEGORY[label],
                severity=CLASS_SEVERITY_PRIOR.get(label, "weak"),
                confidence=round(conf, 3),
                bbox=(10.0 + i, 10.0, 100.0 + i * 5, 100.0),
                frame_index=i,
                frame_width=MOCK_FRAME_WIDTH, frame_height=MOCK_FRAME_HEIGHT,
            ))
        return CVEvidence(detections=dets, frames_analyzed=max(1, count),
                          provider="mock", has_masks=False)


def resolve_device(setting: str) -> str:
    """Map YOLO26_DEVICE (cpu|cuda|auto) to an inference device.

    Never crashes when CUDA is missing: cuda/auto degrade to cpu with a warning.
    """
    want = (setting or "auto").strip().lower()
    if want not in ("cpu", "cuda", "auto"):
        raise ValueError(f"YOLO26_DEVICE must be cpu|cuda|auto, got {setting!r}")
    if want == "cpu":
        return "cpu"
    try:
        import torch
        has_cuda = bool(torch.cuda.is_available())
    except Exception:  # noqa: BLE001 — any torch failure means "no CUDA", never fatal
        has_cuda = False
    if not has_cuda:
        if want == "cuda":
            log.warning("yolo-device cuda requested but unavailable — falling back to cpu")
        return "cpu"
    return "cuda"


def validate_yolo_config() -> dict:
    """Validate everything CV_PROVIDER=yolo needs, with actionable errors.

    Checks checkpoint path → ultralytics import → model load →
    class-name availability. Returns the loaded model + names (single load).
    """
    weights = str(get_settings().YOLO26_SEG_WEIGHTS)
    if not Path(weights).is_file():
        raise RuntimeError(
            f"CV_PROVIDER=yolo needs a trained checkpoint at YOLO26_SEG_WEIGHTS={weights}. "
            "Train/export a yolo26-seg model and place the .pt file there "
            "(see README 'Real YOLO weight setup'); or use CV_PROVIDER=mock for development.")
    try:
        from ultralytics import YOLO  # type: ignore
    except Exception as exc:  # ImportError, OSError (blocked/broken native libs), etc.
        raise RuntimeError(
            "CV_PROVIDER=yolo needs a working 'ultralytics' install "
            "(pip install -r requirements.txt pins the tested ultralytics==8.4.142; "
            f"import failed here with {type(exc).__name__}: {exc}).") from exc
    try:
        model = YOLO(weights)
        names = {int(k): str(v) for k, v in dict(model.names).items()}
    except Exception as exc:
        raise RuntimeError(
            f"Could not load YOLO checkpoint at {weights}: {type(exc).__name__}: {exc}. "
            "Verify the file is a valid Ultralytics .pt checkpoint.") from exc
    if not names:
        raise RuntimeError(f"Checkpoint at {weights} exposes no class names — cannot map detections.")
    return {"model": model, "names": names, "weights": weights}


def yolo_status() -> dict:
    """Lightweight model status for /health. Never loads the checkpoint."""
    try:
        import ultralytics
        version = ultralytics.__version__
    except Exception:  # noqa: BLE001 — status probe must never raise
        return {"installed": False, "version": None, "weights_present": False,
                "device": "cpu", "cuda_available": False}
    weights = str(get_settings().YOLO26_SEG_WEIGHTS)
    try:
        import torch
        cuda = bool(torch.cuda.is_available())
    except Exception:  # noqa: BLE001 — any torch failure means "no CUDA"
        cuda = False
    try:
        device = resolve_device(get_settings().YOLO26_DEVICE)
    except ValueError:
        device = "cpu"
    return {"installed": True, "version": version, "weights_configured": weights,
            "weights_present": Path(weights).is_file(),
            "device": device, "cuda_available": cuda}


def _polygon_area(points: list) -> float:
    """Shoelace area of normalized [[x,y],...] as a frame fraction, clamped 0..1."""
    if len(points) < 3:
        return 0.0
    total = 0.0
    for i in range(len(points)):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % len(points)]
        total += x1 * y2 - x2 * y1
    return min(1.0, max(0.0, abs(total) / 2.0))


def _compact_polygon(raw) -> list:
    """Downsample a normalized polygon to ≤MAX_POLYGON_POINTS rounded points."""
    try:
        pts = [[round(float(x), 4), round(float(y), 4)] for x, y in list(raw)]
    except (TypeError, ValueError):
        return []
    if len(pts) <= MAX_POLYGON_POINTS:
        return pts
    step = len(pts) / MAX_POLYGON_POINTS
    return [pts[int(i * step)] for i in range(MAX_POLYGON_POINTS)]


class YOLO26SegAdapter(SegmentationProvider):
    """Real YOLO26-Seg. Construct only after validate_yolo_config() succeeds."""

    name = "yolo26-seg"

    def __init__(self):
        s = get_settings()
        validated = validate_yolo_config()
        self.model = validated["model"]
        self.names: dict[int, str] = validated["names"]
        self.device = resolve_device(s.YOLO26_DEVICE)
        self.conf = s.YOLO26_CONF
        self.imgsz = s.YOLO26_IMGSZ
        self.iou = s.YOLO26_IOU
        self.max_det = s.YOLO26_MAX_DET
        # fp16 only makes sense on CUDA; silently ignored on CPU.
        self.half = bool(s.YOLO26_HALF and self.device.startswith("cuda"))
        seg_note = "seg" if "seg" in Path(s.YOLO26_SEG_WEIGHTS).stem else "detection"
        log.info("yolo-init weights=%s device=%s conf=%s imgsz=%s flavor~%s",
                 s.YOLO26_SEG_WEIGHTS, self.device, self.conf, self.imgsz, seg_note)

    def infer_frames(self, frames_dir: str, count: int) -> CVEvidence:
        import glob as _glob
        paths = sorted(_glob.glob(f"{frames_dir}/*.jpg"))[:count] or [frames_dir]
        dets: list[CVDetection] = []
        has_masks = False
        for i, p in enumerate(paths):
            for r in self.model.predict(p, conf=self.conf, imgsz=self.imgsz,
                                        iou=self.iou, max_det=self.max_det,
                                        device=self.device, half=self.half, verbose=False):
                try:
                    frame_h, frame_w = r.orig_shape[:2]
                except (AttributeError, TypeError, ValueError):
                    frame_w, frame_h = 0.0, 0.0
                mask_polys = getattr(getattr(r, "masks", None), "xy", None)
                boxes = list(r.boxes or [])
                for j, b in enumerate(boxes):
                    cls = int(b.cls[0])
                    raw_label = self.names.get(cls, str(cls))
                    label = normalize_label(raw_label)
                    category = map_class(label) or UNMAPPED_CATEGORY
                    poly, marea = [], None
                    if mask_polys is not None and j < len(mask_polys):
                        poly = _compact_polygon(mask_polys[j])
                        if poly:
                            marea = _polygon_area(poly)
                            has_masks = True
                    xyxy = [float(v) for v in b.xyxy[0].tolist()]
                    dets.append(CVDetection(
                        label=label or "unknown", category=category,
                        severity=CLASS_SEVERITY_PRIOR.get(label, "weak"),
                        confidence=round(float(b.conf[0]), 3),
                        bbox=(xyxy[0], xyxy[1], xyxy[2], xyxy[3]), frame_index=i,
                        frame_width=float(frame_w), frame_height=float(frame_h),
                        mask_polygon=poly, mask_area=marea))
        if not has_masks:
            log.info("yolo-infer frames=%d detections=%d masks=none (detection-only output; bbox fallback)",
                     len(paths), len(dets))
        return CVEvidence(detections=dets, frames_analyzed=len(paths),
                          provider="yolo26-seg", has_masks=has_masks)


def get_segmentation_provider() -> SegmentationProvider:
    if get_settings().CV_PROVIDER.lower() == "yolo":
        return YOLO26SegAdapter()
    return DevHeuristicAdapter()


# ---------- Severity rules (deterministic, only weak/medium/critical) ----------

def derive_severity(evidence: CVEvidence) -> tuple[dict, Severity, dict[str, Severity]]:
    """Aggregate CV evidence → (counts, overall, per-category). Rules:
    any critical ≥1 → category critical; overall = max category level;
    unmapped findings are excluded (auditable, never scored);
    counts pass through to UI as weak/medium/critical (never raw object counts)."""
    rank = {"weak": 0, "medium": 1, "critical": 2}
    inv = {v: k for k, v in rank.items()}
    counts = {"weak_count": 0, "medium_count": 0, "critical_count": 0}
    for d in evidence.detections:
        if d.category == UNMAPPED_CATEGORY:
            continue
        counts[f"{d.severity}_count"] += 1
    by_cat: dict[str, Severity] = {}
    for cat in CATEGORIES:
        sev: Severity = "weak"
        for d in evidence.detections:
            if d.category == cat and rank[d.severity] > rank[sev]:
                sev = d.severity
        by_cat[cat] = sev
    overall: Severity = inv[max(rank[s] for s in by_cat.values())]  # type: ignore
    if not evidence.detections:
        overall = "weak"
    return counts, overall, by_cat
