"""Local Urban Infrastructure Reasoning Engine.

Deterministic, offline and auditable. Reasons ONLY over structured CV evidence
produced by YOLO26-Seg (or the mock CV provider): detection category,
confidence, bbox area, frame persistence, repetition and co-occurrence.

It never invents observations, requires no network access, API key or credits,
and always returns a validated ReasoningOutput. Only concise, auditable factor
summaries are stored — no hidden chain-of-thought.
"""
from __future__ import annotations

import math

from app.core.config import get_settings
from app.schemas import CategorySeverity, ReasoningOutput, Severity
from app.services import ai

REASONING_SOURCE = "local"

# BBox pixel areas are normalized against the REAL extracted-frame dimensions when
# the evidence carries them; otherwise they fall back to a VGA reference frame so
# that "affected area" stays comparable (mock/legacy evidence has no dimensions).
REFERENCE_FRAME_AREA = 640.0 * 480.0

# Operational impact per category: how urgently a finding disrupts city life.
# Extensible — new categories slot in here with their own weight + templates.
CATEGORY_IMPACT: dict[str, float] = {
    "road_condition": 1.0,
    "drainage": 0.9,
    "waste_management": 0.7,
    "street_infrastructure": 0.6,
}

# Fixed factor weights (sum = 1.0) — transparent and tunable via review, never random.
W_FREQ, W_PERSIST, W_CONF, W_AREA, W_REPEAT = 0.30, 0.25, 0.20, 0.15, 0.10

CATEGORY_NOUNS: dict[str, str] = {
    "road_condition": "road surface",
    "waste_management": "waste",
    "drainage": "drainage",
    "street_infrastructure": "street infrastructure",
}

RECOMMENDATIONS: dict[tuple[str, Severity], str] = {
    ("road_condition", "critical"): "Dispatch a road repair crew to {street} on priority: inspect and repair the damaged road surface, then verify with after-images.",
    ("road_condition", "medium"): "Schedule road surface inspection and patch repair for {street} within the current maintenance cycle.",
    ("road_condition", "weak"): "No road action needed for {street}; continue routine patrol monitoring.",
    ("waste_management", "critical"): "Trigger emergency sanitation response for {street}: clear the dumped waste and investigate illegal dumping at the spot.",
    ("waste_management", "medium"): "Schedule sanitation collection for {street} and monitor for repeat dumping.",
    ("waste_management", "weak"): "No sanitation action needed for {street}; continue routine monitoring.",
    ("drainage", "critical"): "Dispatch a drainage crew to {street} on priority: inspect and clear blocked drains to prevent waterlogging.",
    ("drainage", "medium"): "Schedule drainage inspection and clearing for {street} before peak rainfall.",
    ("drainage", "weak"): "Drainage looks normal for {street}; continue routine monitoring.",
    ("street_infrastructure", "critical"): "Dispatch a civil/electrical inspection team to {street} on priority: assess the damaged infrastructure and make the site safe.",
    ("street_infrastructure", "medium"): "Schedule an infrastructure inspection for {street} (lighting, poles, signage, sidewalks).",
    ("street_infrastructure", "weak"): "Street infrastructure looks normal for {street}; continue routine monitoring.",
}

_SEV_RANK = {"weak": 0, "medium": 1, "critical": 2}


def _num(value: object, default: float = 0.0) -> float:
    try:
        f = float(value)  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return default
    return f if math.isfinite(f) else default


def _sanitize(evidence: ai.CVEvidence | None) -> tuple[list[dict], int, int, int, int]:
    """Coerce raw CV evidence into valid finding dicts.

    Returns (valid, filtered_low_confidence, invalid, unmapped, frames_analyzed).
    Malformed entries are repaired where safe (clamped confidence, ordered
    bbox, real frame dims, compact mask data) or counted as invalid — never crashing.
    Unmapped-vocabulary findings are counted separately and excluded from scoring.
    """
    s = get_settings()
    raw = getattr(evidence, "detections", None) or []
    frames = int(getattr(evidence, "frames_analyzed", 0) or 0)
    valid: list[dict] = []
    filtered = 0
    invalid = 0
    unmapped = 0
    for d in raw:
        if not isinstance(d, object) or d is None:
            invalid += 1
            continue
        label = str(getattr(d, "label", None) or "unknown").strip() or "unknown"
        category = getattr(d, "category", None)
        if category == ai.UNMAPPED_CATEGORY or category not in ai.CATEGORIES:
            unmapped += 1
            continue
        conf = _num(getattr(d, "confidence", 0.0))  # non-finite → 0.0
        conf = min(1.0, max(0.0, conf))
        bbox = getattr(d, "bbox", None) or (0.0, 0.0, 0.0, 0.0)
        try:
            x1, y1, x2, y2 = (float(v) for v in list(bbox)[:4])
            if not all(math.isfinite(v) for v in (x1, y1, x2, y2)):
                raise ValueError
        except (TypeError, ValueError):
            invalid += 1
            continue
        x1, x2 = min(x1, x2), max(x1, x2)
        y1, y2 = min(y1, y2), max(y1, y2)
        sev = getattr(d, "severity", None)
        if sev not in _SEV_RANK:
            sev = ai.CLASS_SEVERITY_PRIOR.get(ai.normalize_label(label), "weak")
        if conf < s.YOLO26_CONF:
            filtered += 1
            continue
        frame = getattr(d, "frame_index", 0)
        try:
            frame = int(frame)
        except (TypeError, ValueError):
            frame = 0
        fw, fh = _num(getattr(d, "frame_width", 0.0)), _num(getattr(d, "frame_height", 0.0))
        fw, fh = (fw if fw > 0 else 0.0), (fh if fh > 0 else 0.0)
        marea = _num(getattr(d, "mask_area", None) if getattr(d, "mask_area", None) is not None else float("nan"),
                     default=float("nan"))
        marea = min(1.0, max(0.0, marea)) if math.isfinite(marea) else None
        valid.append({"label": label, "category": category, "severity": sev,
                      "conf": conf, "area": max(0.0, x2 - x1) * max(0.0, y2 - y1),
                      "frame": frame, "bbox": (x1, y1, x2, y2),
                      "frame_width": fw, "frame_height": fh, "mask_area": marea})
    return valid, filtered, invalid, unmapped, frames


def _norm_area(e: dict) -> float:
    """Affected area as a frame fraction: real mask area first, then bbox over the
    REAL frame dimensions, then the VGA reference fallback (mock/legacy evidence)."""
    if e.get("mask_area") is not None:
        return min(1.0, max(0.0, e["mask_area"]))
    fw, fh = e.get("frame_width", 0.0), e.get("frame_height", 0.0)
    if fw > 0 and fh > 0:
        return min(1.0, max(0.0, e["area"] / (fw * fh)))
    return min(1.0, max(0.0, e["area"] / REFERENCE_FRAME_AREA))


def _score_category(category: str, entries: list[dict], frames_analyzed: int) -> tuple[float, Severity, str]:
    """Factor scoring → (score, severity, auditable summary). Fully deterministic."""
    s = get_settings()
    n = len(entries)
    if n == 0:
        return 0.0, "weak", "no findings"
    frames_hit = len({e["frame"] for e in entries})
    persist = frames_hit / max(1, frames_analyzed)
    mean_conf = sum(e["conf"] for e in entries) / n
    total_norm = sum(_norm_area(e) for e in entries)
    area_term = min(1.0, total_norm / 0.25)
    freq_term = min(1.0, n / 5.0)
    distinct = len({e["label"] for e in entries})
    repeat = (n - distinct) / n
    raw = (W_FREQ * freq_term + W_PERSIST * persist + W_CONF * mean_conf
           + W_AREA * area_term + W_REPEAT * repeat)
    score = raw * (0.75 + 0.25 * CATEGORY_IMPACT.get(category, 0.6))
    severity: Severity = ("critical" if score >= s.REASONING_SCORE_CRITICAL
                          else "medium" if score >= s.REASONING_SCORE_MEDIUM else "weak")
    drivers = [name for name, contrib in
               (("frequency", W_FREQ * freq_term), ("persistence", W_PERSIST * persist),
                ("confidence", W_CONF * mean_conf), ("area", W_AREA * area_term),
                ("repetition", W_REPEAT * repeat)) if contrib >= 0.05]
    area_pct = min(1.0, total_norm)
    summary = (f"{n} finding(s), {frames_hit}/{max(1, frames_analyzed)} frames, "
               f"mean conf {mean_conf:.2f}, area {area_pct:.0%} → "
               f"{severity.capitalize()} ({', '.join(drivers) if drivers else 'limited signal'})")
    return score, severity, summary


def _request_recommended(overall: Severity, counts: dict) -> bool:
    """Critical → always; Weak → never; Medium → configurable finding threshold."""
    if overall == "critical":
        return True
    if overall == "weak":
        return False
    return (counts["medium_count"] + counts["critical_count"]) >= get_settings().MEDIUM_REQUEST_MIN_FINDINGS


def reason(evidence: ai.CVEvidence | None, street_name: str) -> ReasoningOutput:
    """Run the local reasoning engine over CV evidence → validated structured output."""
    street = (street_name or "unknown street").strip() or "unknown street"
    valid, filtered, invalid, unmapped, frames = _sanitize(evidence)

    if not valid:
        detail = f"{invalid} invalid" if invalid else "no detections"
        if filtered:
            detail += f", {filtered} below-confidence finding(s) filtered"
        if unmapped:
            detail += f", {unmapped} unmapped-vocabulary finding(s) excluded"
        cats = {c: "weak" for c in ai.CATEGORIES}
        return ReasoningOutput(
            overall_severity="weak", weak_count=0, medium_count=0, critical_count=0,
            categories=CategorySeverity(**cats),
            reason=(f"{street}: no actionable CV evidence ({detail}). "
                    "Overall Weak; continue routine monitoring."),
            recommendation=f"No municipal action required. Continue routine monitoring of {street}.",
            municipal_request_recommended=False,
        )

    # Severity counts reuse the deterministic CV aggregation (per-finding levels).
    cv = ai.CVEvidence(
        detections=[ai.CVDetection(label=e["label"], category=e["category"], severity=e["severity"],
                                   confidence=e["conf"], bbox=e["bbox"], frame_index=e["frame"],
                                   frame_width=e["frame_width"], frame_height=e["frame_height"])
                    for e in valid],
        frames_analyzed=frames, provider=getattr(evidence, "provider", "mock") or "mock")
    counts, _, _ = ai.derive_severity(cv)

    scored: dict[str, tuple[float, Severity, str]] = {}
    for cat in ai.CATEGORIES:
        scored[cat] = _score_category(cat, [e for e in valid if e["category"] == cat], frames)
    overall: Severity = max((sev for _, sev, _ in scored.values()),
                            key=lambda v: _SEV_RANK[v])  # type: ignore[arg-type]

    active = [(cat, sev, summ) for cat, (_, sev, summ) in scored.items()
              if any(e["category"] == cat for e in valid)]
    parts = [f"{CATEGORY_NOUNS.get(cat, cat)}: {summ}" for cat, _, summ in active]
    reason = (f"{street}: {len(valid)} valid finding(s) across {max(1, frames)} frame(s). "
              + "; ".join(parts)
              + (f"; {unmapped} unmapped-vocabulary finding(s) excluded from scoring" if unmapped else "")
              + f". Overall {overall.capitalize()}; worst category drives priority.")

    # Worst category wins; ties break by score, then fixed category order.
    # max() returns the first maximal item in iteration (CATEGORIES) order.
    worst = max(scored, key=lambda cat: (_SEV_RANK[scored[cat][1]], scored[cat][0]))
    recommendation = RECOMMENDATIONS[(worst, scored[worst][1])].format(street=street)
    others = [(cat, sev) for cat, (_, sev, _) in scored.items()
              if cat != worst and sev in ("medium", "critical")]
    if others:
        extra = ", ".join(f"{CATEGORY_NOUNS.get(c, c)} ({v})" for c, v in others)
        recommendation += f" Combine with {extra} action in the same visit to {street}."

    return ReasoningOutput(
        overall_severity=overall,
        weak_count=counts["weak_count"], medium_count=counts["medium_count"],
        critical_count=counts["critical_count"],
        categories=CategorySeverity(**{c: scored[c][1] for c in ai.CATEGORIES}),
        reason=reason,
        recommendation=recommendation,
        municipal_request_recommended=_request_recommended(overall, counts),
    )
