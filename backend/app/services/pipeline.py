"""End-to-end analysis pipeline: validate → frames → YOLO → severity → local reasoning → persist."""
from __future__ import annotations

import json
import shutil
from pathlib import Path

from sqlalchemy.orm import Session

from app.core.config import get_settings
from app.core.logging import get_logger
from app.models.analysis import Analysis, Detection, Incident
from app.models.geo import Street, Video
from app.services import ai, reasoning
from app.services.storage import open_stream, resolve_path
from app.services.video_pipeline import extract_frames, validate_video

log = get_logger("pipeline")


def _stage_video(video: Video, analysis_id: int) -> tuple[Path | None, Path | None]:
    """Return (processable path, temp dir to clean up). S3 objects stream to local temp."""
    if video.storage_key.startswith("s3://"):
        tmpdir = Path(get_settings().STORAGE_DIR) / "tmp" / f"analysis_{analysis_id}"
        tmpdir.mkdir(parents=True, exist_ok=True)
        target = tmpdir / "source.mp4"
        with open_stream(video.storage_key) as src, target.open("wb") as dst:
            shutil.copyfileobj(src, dst)
        return target, tmpdir
    path = resolve_path(video.storage_key)
    return (path if path and path.exists() else None), None


def run_analysis(db: Session, analysis_id: int) -> None:
    a = db.query(Analysis).filter(Analysis.id == analysis_id).first()
    if not a:
        return
    try:
        a.status = "running"
        db.commit()
        street = db.query(Street).filter(Street.id == a.street_id).first()
        video = db.query(Video).filter(Video.id == a.video_id).first() if a.video_id else None

        frames_dir = Path(f"./storage/frames/analysis_{a.id}")
        count = 0
        frame_w, frame_h = 0.0, 0.0
        tmpdir: Path | None = None
        try:
            if video:
                vpath, tmpdir = _stage_video(video, a.id)
                if vpath is None:
                    raise RuntimeError("video file unavailable from storage")
                ok, msg, dur = validate_video(vpath, video.size_bytes)
                if not ok:
                    raise RuntimeError(f"video invalid: {msg}")
                if dur:
                    video.duration_s = dur
                count, frame_w, frame_h = extract_frames(vpath, frames_dir)
        finally:
            if tmpdir is not None:
                shutil.rmtree(tmpdir, ignore_errors=True)

        provider = ai.get_segmentation_provider()
        evidence = provider.infer_frames(str(frames_dir), count or 4)
        reasoned = reasoning.reason(evidence, street.name if street else "unknown street")
        source = reasoning.REASONING_SOURCE

        a.status = "done"
        a.overall_severity = reasoned.overall_severity
        a.weak_count, a.medium_count, a.critical_count = (
            reasoned.weak_count, reasoned.medium_count, reasoned.critical_count)
        a.cat_road = reasoned.categories.road_condition
        a.cat_waste = reasoned.categories.waste_management
        a.cat_drainage = reasoned.categories.drainage
        a.cat_infra = reasoned.categories.street_infrastructure
        a.reason = reasoned.reason
        a.recommendation = reasoned.recommendation
        a.request_recommended = reasoned.municipal_request_recommended
        a.reasoning_source = source
        db.commit()

        for d in evidence.detections:  # raw evidence → internal table only
            db.add(Detection(analysis_id=a.id, frame_index=d.frame_index, label=d.label,
                             category=d.category, severity=d.severity,
                             confidence=d.confidence, x1=d.bbox[0], y1=d.bbox[1],
                             x2=d.bbox[2], y2=d.bbox[3],
                             frame_width=d.frame_width or None,
                             frame_height=d.frame_height or None,
                             mask_area=d.mask_area,
                             mask_polygon=json.dumps(d.mask_polygon) if d.mask_polygon else None))
        if not db.query(Incident).filter(Incident.analysis_id == a.id).first():
            db.add(Incident(analysis_id=a.id, street_id=a.street_id, severity=a.overall_severity or "weak"))
        db.commit()
        log.info("analysis=%d severity=%s source=%s masks=%s extracted=%dx%d",
                 a.id, a.overall_severity, source, evidence.has_masks, frame_w, frame_h)
    except Exception as exc:  # noqa: BLE001 — pipeline must never crash; error is recorded on the analysis
        log.warning("analysis-failed id=%d err=%s", analysis_id, type(exc).__name__)
        a.status = "failed"
        a.error = str(exc)[:500]
        db.commit()
