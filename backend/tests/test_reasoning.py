"""Local Urban Infrastructure Reasoning Engine tests.

Covers: weak/medium/critical, confidence/persistence/area impact,
multi-category, no detections, invalid evidence, determinism,
municipal request policy, mock CV compatibility, schema validation.
"""
from app.schemas import ReasoningOutput
from app.services import ai, reasoning


def det(label, category, severity, conf, side=90.0, frame=0):
    return ai.CVDetection(label=label, category=category, severity=severity,
                          confidence=conf, bbox=(0.0, 0.0, side, side),
                          frame_index=frame)


def ev(dets, frames):
    return ai.CVEvidence(detections=dets, frames_analyzed=frames, provider="mock")


def test_weak_severity():
    out = reasoning.reason(ev([det("litter", "waste_management", "weak", 0.40)], 6), "MG Road")
    assert out.overall_severity == "weak"
    assert out.categories.waste_management == "weak"
    assert out.municipal_request_recommended is False
    assert "MG Road" in out.reason and "MG Road" in out.recommendation


def test_medium_severity():
    dets = [det("crack", "road_condition", "medium", 0.70, frame=f) for f in (0, 1)]
    out = reasoning.reason(ev(dets, 4), "Brigade Road")
    assert out.overall_severity == "medium"
    assert out.categories.road_condition == "medium"
    assert "maintenance" in out.recommendation.lower() or "inspect" in out.recommendation.lower()


def test_critical_severity():
    dets = [det("pothole", "road_condition", "critical", 0.90, frame=f) for f in range(5)]
    out = reasoning.reason(ev(dets, 5), "Outer Ring Road")
    assert out.overall_severity == "critical"
    assert out.categories.road_condition == "critical"
    assert out.municipal_request_recommended is True
    assert "repair crew" in out.recommendation or "priority" in out.recommendation


def test_confidence_impact():
    high = reasoning.reason(ev([det("crack", "road_condition", "medium", 0.95)], 2), "S")
    low = reasoning.reason(ev([det("crack", "road_condition", "medium", 0.40)], 2), "S")
    assert high.overall_severity == "medium"
    assert low.overall_severity == "weak"


def test_persistence_impact():
    spread = reasoning.reason(ev([det("crack", "road_condition", "medium", 0.70)], 1), "S")
    fleeting = reasoning.reason(ev([det("crack", "road_condition", "medium", 0.70)], 6), "S")
    rank = {"weak": 0, "medium": 1, "critical": 2}
    assert rank[spread.overall_severity] > rank[fleeting.overall_severity]


def test_area_impact():
    small = reasoning.reason(ev([det("litter", "waste_management", "weak", 0.50, side=90.0)], 2), "S")
    huge = reasoning.reason(ev([det("litter", "waste_management", "weak", 0.50, side=500.0)], 2), "S")
    assert small.overall_severity == "weak"
    assert huge.overall_severity == "medium"


def test_multiple_categories_and_cooccurrence():
    dets = ([det("crack", "road_condition", "medium", 0.65, frame=f) for f in (0, 1)]
            + [det("clogged_drain", "drainage", "medium", 0.65, frame=f) for f in (0, 1)])
    out = reasoning.reason(ev(dets, 2), "Kanakapura Road")
    assert out.categories.road_condition == "medium"
    assert out.categories.drainage == "medium"
    assert "Combine" in out.recommendation  # co-occurrence grounded in evidence


def test_no_detections():
    out = reasoning.reason(ev([], 8), "Empty Street")
    assert out.overall_severity == "weak"
    assert (out.weak_count, out.medium_count, out.critical_count) == (0, 0, 0)
    assert out.municipal_request_recommended is False
    assert "No municipal action required" in out.recommendation


def test_low_confidence_filtered():
    out = reasoning.reason(ev([det("pothole", "road_condition", "critical", 0.10)], 4), "S")
    assert out.overall_severity == "weak"  # filtered → insufficient evidence
    assert "filtered" in out.reason


def test_invalid_evidence_never_crashes():
    assert reasoning.reason(None, "S").overall_severity == "weak"
    weird = ai.CVEvidence(detections=["junk", None, 42], frames_analyzed=0, provider="mock")
    out = reasoning.reason(weird, "S")
    assert out.overall_severity == "weak"
    # Unknown vocabulary is excluded from scoring (auditable, never silently relabeled)
    ufo = ev([det("ufo", "space", "critical", 0.90, side=50.0)], 1)
    out2 = reasoning.reason(ufo, "S")
    assert out2.overall_severity == "weak"
    assert (out2.weak_count, out2.medium_count, out2.critical_count) == (0, 0, 0)
    assert "unmapped" in out2.reason


def test_deterministic_identical_inputs():
    dets = [det("pothole", "road_condition", "critical", 0.87, frame=f) for f in range(3)]
    a = reasoning.reason(ev(dets, 3), "Same Street")
    b = reasoning.reason(ev(dets, 3), "Same Street")
    assert a.model_dump() == b.model_dump()


def test_request_policy():
    crit = reasoning.reason(ev([det("pothole", "road_condition", "critical", 0.9, frame=f)
                                for f in range(5)], 5), "S")
    assert crit.municipal_request_recommended is True
    weak = reasoning.reason(ev([det("litter", "waste_management", "weak", 0.4)], 6), "S")
    assert weak.municipal_request_recommended is False
    two = reasoning.reason(ev([det("crack", "road_condition", "medium", 0.7, frame=f)
                               for f in (0, 1)], 2), "S")
    three = reasoning.reason(ev([det("crack", "road_condition", "medium", 0.7, frame=f)
                                 for f in (0, 1, 2)], 3), "S")
    assert two.municipal_request_recommended is False   # below medium threshold
    assert three.municipal_request_recommended is True  # meets medium threshold


def test_mock_cv_compatibility():
    mock = ai.DevHeuristicAdapter().infer_frames("some/street/dir", 4)
    out = reasoning.reason(mock, "Mock Street")
    assert isinstance(out, ReasoningOutput)
    assert out.overall_severity in ("weak", "medium", "critical")
    # Reason explains WHY without exposing chain-of-thought internals
    assert "finding" in out.reason.lower()


def test_schema_rejects_invented_severity():
    import pytest
    from pydantic import ValidationError

    with pytest.raises(ValidationError):
        ReasoningOutput.model_validate({
            "overall_severity": "severe", "weak_count": 0, "medium_count": 0,
            "critical_count": 0,
            "categories": {"road_condition": "weak", "waste_management": "weak",
                           "drainage": "weak", "street_infrastructure": "weak"},
            "reason": "x" * 20, "recommendation": "y" * 20,
            "municipal_request_recommended": False})


def _entry(label, conf, area, frame):
    return {"label": label, "category": "road_condition", "severity": "medium",
            "conf": conf, "area": area, "frame": frame, "bbox": (0.0, 0.0, 90.0, 90.0)}


def test_operational_impact_changes_severity():
    from app.services.reasoning import _score_category
    entries = [_entry("crack", 0.80, 8100.0, f) for f in range(3)]
    road_score, road_sev, _ = _score_category("road_condition", entries, 3)
    infra_score, infra_sev, _ = _score_category("street_infrastructure", entries, 3)
    assert road_score > infra_score  # identical evidence, higher-impact category scores higher
    rank = {"weak": 0, "medium": 1, "critical": 2}
    assert rank[road_sev] >= rank[infra_sev]


def test_repetition_changes_score():
    from app.services.reasoning import _score_category
    same = [_entry("pothole", 0.70, 8100.0, f) for f in range(4)]
    varied = [{**_entry(f"issue{i}", 0.70, 8100.0, f)} for i, f in enumerate(range(4))]
    s_same, _, _ = _score_category("road_condition", same, 4)
    s_varied, _, _ = _score_category("road_condition", varied, 4)
    assert s_same > s_varied  # repeated same defect persists harder than scattered ones


def test_no_unsupported_claims_in_output():
    dets = [det("pothole", "road_condition", "critical", 0.90, frame=f) for f in range(5)]
    out = reasoning.reason(ev(dets, 5), "Test Road")
    text = (out.reason + " " + out.recommendation).lower()
    for banned in ("waste", "drainage", "sanitation", "street infrastructure",
                   "dumping", "waterlog", "electrical"):
        assert banned not in text, f"unsupported claim leaked: {banned}"
