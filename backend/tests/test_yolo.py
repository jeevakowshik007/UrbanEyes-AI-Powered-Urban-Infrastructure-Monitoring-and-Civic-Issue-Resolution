"""YOLO26-Seg integration tests.

Uses a stubbed `ultralytics` module (clearly a test seam, NOT real inference)
for adapter/config/mask tests. A real-inference smoke test exists but SKIPS
unless a checkpoint is actually present — it must never fake a model run.
"""
import sys
import types

import pytest

from app.services import ai

# ---------- Stub ultralytics seam ----------

class _Val:
    def __init__(self, v):
        self._v = v

    def __getitem__(self, i):
        v = self._v[i]
        return _Val(v) if isinstance(v, list) else v

    def tolist(self):
        return self._v

    def __float__(self):
        return float(self._v)

    def __int__(self):
        return int(self._v)


class _FakeBox:
    def __init__(self, cls, conf, xyxy):
        self.cls = _Val([cls])
        self.conf = _Val([conf])
        self.xyxy = _Val([xyxy])


class _FakeMasks:
    def __init__(self, polys):
        self.xy = polys


class _FakeResult:
    def __init__(self, boxes, polys="default", shape=(480, 640)):
        self.boxes = boxes
        self.masks = None if polys is None else _FakeMasks(polys)
        self.orig_shape = shape
        self.names = {0: "Pothole", 1: "Space Junk"}


class _FakeYOLO:
    last_kwargs = None

    def __init__(self, path):
        if not str(path).endswith(".pt"):
            raise FileNotFoundError(path)
        self.path = str(path)
        self.names = {0: "Pothole", 1: "Space Junk"}

    def predict(self, p, **kw):
        _FakeYOLO.last_kwargs = {"path": p, **kw}
        return [_FakeResult(
            [_FakeBox(0, 0.9, [10, 10, 110, 60]), _FakeBox(1, 0.8, [0, 0, 50, 50])],
            polys=[[[0.1, 0.1], [0.4, 0.1], [0.4, 0.3], [0.1, 0.3]]])]


def _stub_ultralytics(monkeypatch):
    mod = types.ModuleType("ultralytics")
    mod.YOLO = _FakeYOLO
    mod.__version__ = "stub"
    monkeypatch.setitem(sys.modules, "ultralytics", mod)
    return mod


def _frame_dir(tmp_path):
    d = tmp_path / "frames"
    d.mkdir()
    (d / "frame_0000.jpg").write_bytes(b"fake-jpg")
    return d


# ---------- Config validation ----------

def test_yolo_missing_weights_fails_actionably(monkeypatch, tmp_path):
    from app.core.config import get_settings
    monkeypatch.setattr(get_settings(), "CV_PROVIDER", "yolo")
    monkeypatch.setattr(get_settings(), "YOLO26_SEG_WEIGHTS", str(tmp_path / "nope.pt"))
    with pytest.raises(RuntimeError, match="YOLO26_SEG_WEIGHTS"):
        ai.get_segmentation_provider()


def test_mock_needs_neither_package_nor_weights(monkeypatch):
    from app.core.config import get_settings
    monkeypatch.setitem(sys.modules, "ultralytics", None)  # simulate: not installed
    monkeypatch.setattr(get_settings(), "CV_PROVIDER", "mock")
    provider = ai.get_segmentation_provider()
    assert provider.name == "mock"
    ev = provider.infer_frames("anydir", 3)
    assert ev.provider == "mock" and len(ev.detections) >= 1


def test_mock_carries_frame_dimensions():
    ev = ai.DevHeuristicAdapter().infer_frames("anydir", 3)
    assert all(d.frame_width == 640.0 and d.frame_height == 480.0 for d in ev.detections)
    assert ev.has_masks is False


# ---------- Adapter seam (stubbed ultralytics, NOT real inference) ----------

def test_adapter_consumes_boxes_masks_dims(monkeypatch, tmp_path):
    from app.core.config import get_settings
    _stub_ultralytics(monkeypatch)
    pt = tmp_path / "test-seg.pt"
    pt.write_bytes(b"stub-weights")
    monkeypatch.setattr(get_settings(), "CV_PROVIDER", "yolo")
    monkeypatch.setattr(get_settings(), "YOLO26_SEG_WEIGHTS", str(pt))
    adapter = ai.get_segmentation_provider()
    assert adapter.name == "yolo26-seg"
    ev = adapter.infer_frames(str(_frame_dir(tmp_path)), 4)
    assert ev.provider == "yolo26-seg" and ev.has_masks is True
    pothole, junk = ev.detections
    assert (pothole.label, pothole.category) == ("pothole", "road_condition")
    assert (pothole.frame_width, pothole.frame_height) == (640.0, 480.0)
    assert len(pothole.mask_polygon) == 4  # compact, not a raw tensor
    assert pothole.mask_area == pytest.approx(0.06)  # 0.3 x 0.2 normalized
    assert (junk.label, junk.category) == ("space_junk", ai.UNMAPPED_CATEGORY)


def test_adapter_detection_only_model_uses_bbox_fallback(monkeypatch, tmp_path):
    from app.core.config import get_settings
    _stub_ultralytics(monkeypatch)

    orig_predict = _FakeYOLO.predict

    def no_masks(self, p, **kw):
        _FakeYOLO.last_kwargs = kw
        return [_FakeResult([_FakeBox(2, 0.7, [0, 0, 64, 64])], polys=None)]

    monkeypatch.setattr(_FakeYOLO, "predict", no_masks)
    try:
        pt = tmp_path / "det.pt"
        pt.write_bytes(b"x")
        monkeypatch.setattr(get_settings(), "CV_PROVIDER", "yolo")
        monkeypatch.setattr(get_settings(), "YOLO26_SEG_WEIGHTS", str(pt))
        ev = ai.get_segmentation_provider().infer_frames(str(_frame_dir(tmp_path)), 1)
        assert ev.has_masks is False
        assert ev.detections[0].mask_area is None
        assert ev.detections[0].mask_polygon == []
    finally:
        monkeypatch.setattr(_FakeYOLO, "predict", orig_predict)


def test_adapter_forwards_inference_settings(monkeypatch, tmp_path):
    from app.core.config import get_settings
    _stub_ultralytics(monkeypatch)
    pt = tmp_path / "s.pt"
    pt.write_bytes(b"x")
    s = get_settings()
    monkeypatch.setattr(s, "CV_PROVIDER", "yolo")
    monkeypatch.setattr(s, "YOLO26_SEG_WEIGHTS", str(pt))
    monkeypatch.setattr(s, "YOLO26_CONF", 0.5)
    monkeypatch.setattr(s, "YOLO26_IMGSZ", 512)
    ai.get_segmentation_provider().infer_frames(str(_frame_dir(tmp_path)), 1)
    kw = _FakeYOLO.last_kwargs
    assert kw["conf"] == 0.5 and kw["imgsz"] == 512
    assert {"iou", "max_det", "device", "half"} <= set(kw)


# ---------- Class mapping ----------

def test_class_mapping_known_unknown_normalization():
    assert ai.map_class("pothole") == "road_condition"
    assert ai.map_class("Pothole") == "road_condition"      # case
    assert ai.map_class("Road Damage") == "road_condition"  # space
    assert ai.map_class("CLOGGED_DRAIN") == "drainage"
    assert ai.map_class("space junk") is None               # unknown → unmapped
    assert ai.map_class("") is None
    assert ai.map_class("!!!") is None


# ---------- Devices ----------

def test_device_resolution():
    assert ai.resolve_device("cpu") == "cpu"
    assert ai.resolve_device("auto") == "cpu"   # this box has no CUDA
    assert ai.resolve_device("cuda") == "cpu"   # graceful fallback, no crash
    with pytest.raises(ValueError, match="cpu\\|cuda\\|auto"):
        ai.resolve_device("tpu")


def test_broken_native_torch_degrades_to_cpu(monkeypatch):
    """Regression: on locked-down machines `import torch` can raise OSError
    (blocked DLL), not ImportError — device resolution must still fall back."""
    import sys
    import types

    def _boom():
        raise OSError("Application Control policy blocked torch DLL")

    fake = types.ModuleType("torch")
    fake.cuda = types.SimpleNamespace(is_available=_boom)
    monkeypatch.setitem(sys.modules, "torch", fake)
    assert ai.resolve_device("auto") == "cpu"
    assert ai.resolve_device("cuda") == "cpu"


# ---------- Frame dimensions / sampling ----------

def _mp4(tmp_path):
    import cv2
    import numpy as np
    p = tmp_path / "v.mp4"
    w = cv2.VideoWriter(str(p), cv2.VideoWriter_fourcc(*"mp4v"), 5, (64, 48))
    for i in range(12):
        w.write(np.full((48, 64, 3), i * 20, dtype=np.uint8))
    w.release()
    return p


def test_extract_frames_reports_real_dimensions(tmp_path):
    from app.services.video_pipeline import extract_frames
    n, fw, fh = extract_frames(_mp4(tmp_path), tmp_path / "f1")
    assert (n, fw, fh) == (12, 64.0, 48.0)


def test_frame_sampling_deterministic(tmp_path):
    import hashlib

    from app.services.video_pipeline import extract_frames
    src = _mp4(tmp_path)
    n1, _, _ = extract_frames(src, tmp_path / "a")
    n2, _, _ = extract_frames(src, tmp_path / "b")
    assert n1 == n2 >= 1

    def frame_hash(d):
        return hashlib.sha256((d / "frame_0000.jpg").read_bytes()).hexdigest()

    assert frame_hash(tmp_path / "a") == frame_hash(tmp_path / "b")


def test_normalized_area_uses_real_dimensions():
    from app.services.reasoning import _score_category

    def entries(fw, fh):
        return [{"label": "x", "category": "road_condition", "severity": "weak",
                 "conf": 0.8, "area": 10000.0, "frame": 0, "bbox": (0, 0, 100, 100),
                 "frame_width": fw, "frame_height": fh, "mask_area": None}]

    small_score, _, small_sum = _score_category("road_condition", entries(640.0, 480.0), 1)
    big_score, _, big_sum = _score_category("road_condition", entries(1280.0, 960.0), 1)
    assert small_score > big_score  # identical box, smaller frame → relatively larger
    assert "3%" in small_sum and "1%" in big_sum


def test_mask_area_preferred_over_bbox():
    from app.services.reasoning import _norm_area
    e = {"area": 200000.0, "frame_width": 640.0, "frame_height": 480.0, "mask_area": 0.02}
    assert _norm_area(e) == pytest.approx(0.02)


# ---------- Malformed video / inference failure ----------

def test_malformed_videos_rejected(tmp_path):

    from app.services.video_pipeline import validate_video
    corrupt = tmp_path / "c.mp4"
    corrupt.write_bytes(b"\x00\x01not-a-video" * 100)
    assert validate_video(corrupt, 1000)[0] is False
    empty = tmp_path / "e.mp4"
    empty.write_bytes(b"")
    assert validate_video(empty, 0)[0] is False


def test_inference_failure_marks_analysis_failed(monkeypatch):
    from app.db.session import SessionLocal
    from app.models.analysis import Analysis
    from app.services.pipeline import run_analysis

    class _Boom(ai.SegmentationProvider):
        name = "boom"

        def infer_frames(self, frames_dir, count):
            raise RuntimeError("simulated inference crash")

    monkeypatch.setattr(ai, "get_segmentation_provider", lambda: _Boom())
    db = SessionLocal()
    try:
        a = Analysis(street_id=1, video_id=None, created_by=1, status="queued")
        db.add(a)
        db.commit()
        run_analysis(db, a.id)
        db.refresh(a)
        assert a.status == "failed" and a.error
    finally:
        db.close()


# ---------- Real-model honesty gate ----------

def test_real_inference_smoke_or_skip(tmp_path):
    """Runs REAL YOLO26-Seg inference only if a checkpoint is actually present."""
    from pathlib import Path

    from app.core.config import get_settings
    weights = Path(get_settings().YOLO26_SEG_WEIGHTS)
    if not weights.is_file():
        pytest.skip("REAL MODEL INFERENCE NOT EXECUTED — CHECKPOINT NOT PRESENT")
    adapter = ai.YOLO26SegAdapter()
    d = tmp_path / "f"
    d.mkdir()
    (d / "frame_0000.jpg").write_bytes(b"x")
    ev = adapter.infer_frames(str(d), 1)
    assert isinstance(ev, ai.CVEvidence)
