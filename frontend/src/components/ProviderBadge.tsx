import { useEffect, useState } from 'react';
import api from '../services/api';

/** Honest AI-mode indicator: never lets mock vision pass as real inference. */
export default function ProviderBadge() {
  const [h, setH] = useState<{
    cv_provider?: string; reasoning_provider?: string;
    yolo?: { installed?: boolean; version?: string | null; weights_present?: boolean; device?: string } | null;
  } | null>(null);
  useEffect(() => {
    api.get('/health').then((r) => setH(r.data)).catch(() => null);
  }, []);
  if (!h) return null;
  const mock = h.cv_provider !== 'yolo';
  const modelStatus = h.yolo?.weights_present
    ? `Checkpoint installed (ultralytics ${h.yolo.version ?? '?'}, ${h.yolo.device ?? 'cpu'}).`
    : 'No checkpoint installed — set YOLO26_SEG_WEIGHTS with a trained yolo26-seg .pt to enable real vision.';
  return (
    <div
      className="text-xs font-semibold px-3 py-1.5 rounded-xl inline-flex items-center gap-2"
      style={{
        background: mock ? 'rgba(201,162,39,.12)' : 'rgba(34,160,107,.12)',
        color: mock ? '#8a6d1a' : '#14714c',
        border: `1px solid ${mock ? '#D8C46A' : '#7FBF9B'}`,
      }}
      title={mock
        ? `Development mode: detections are deterministic mock evidence, reasoning is the local engine. ${modelStatus}`
        : `Production vision: YOLO26-Seg inference with the local reasoning engine. ${modelStatus}`}
    >
      <span className="w-2 h-2 rounded-full" style={{ background: mock ? '#c9a227' : '#22a06b' }} />
      {mock ? 'Development vision (mock detections)' : 'YOLO26-Seg vision'}
      <span className="opacity-60">·</span> Local infrastructure reasoning
    </div>
  );
}
