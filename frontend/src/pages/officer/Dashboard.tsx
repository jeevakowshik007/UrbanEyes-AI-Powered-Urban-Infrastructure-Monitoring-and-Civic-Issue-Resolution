import { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import api from '../../services/api';
import UrbanOpsMap, { MapPoint } from '../../components/UrbanOpsMap';
import ProviderBadge from '../../components/ProviderBadge';
import { GlassCard, SeverityBadge, Stage, Empty } from '../../components/ui';

export default function OfficerDashboard() {
  const [reqs, setReqs] = useState<any[]>([]);
  const [streets, setStreets] = useState<any[]>([]);
  const [me, setMe] = useState<any>(null);

  useEffect(() => {
    (async () => {
      const [r, s, m] = await Promise.all([
        api.get('/api/v1/requests'), api.get('/api/v1/streets'), api.get('/api/v1/auth/me'),
      ]);
      setReqs(r.data);
      setStreets(s.data);
      setMe(m.data);
    })().catch(console.error);
  }, []);

  const open = reqs.filter((r) => !['resolved', 'rejected'].includes(r.status));
  const critical = open.filter((r) => r.severity === 'critical');
  const mine = reqs.filter((r) => r.assigned_to === me?.id && !['resolved', 'rejected'].includes(r.status));
  const coord = new Map(streets.map((s: any) => [s.id, s]));
  const points: MapPoint[] = open
    .filter((r) => coord.get(r.street_id))
    .map((r) => {
      const s = coord.get(r.street_id);
      return { id: r.id, lat: s.latitude, lon: s.longitude, severity: r.severity, label: `${r.code} — ${s.name} — ${r.status}`, kind: 'request' as const };
    });

  return (
    <Stage>
      <ProviderBadge />
      <h1 className="font-display text-2xl font-bold">What needs my attention?</h1>
      <p className="text-sm text-slate-500">
        {open.length} open requests · {critical.length} critical · {mine.length} assigned to you
      </p>

      {critical.length > 0 && (
        <GlassCard className="border-l-4" >
          <div className="font-semibold text-sm mb-2 text-critical">⚠ Critical requests first</div>
          {critical.map((r) => (
            <Link key={r.id} to={`/officer/requests/${r.id}`} className="flex items-center gap-2 text-sm py-1.5 border-b border-slate-100 last:border-0">
              <SeverityBadge level="critical" size="sm" />
              <b className="font-mono">{r.code}</b>
              <span className="text-slate-500">{r.status.replace('_', ' ')}</span>
            </Link>
          ))}
        </GlassCard>
      )}

      <GlassCard>
        <div className="font-semibold mb-3 text-sm">Open request locations</div>
        {points.length === 0 ? <Empty msg="Queue is clear." /> : <UrbanOpsMap points={points} height={360} />}
      </GlassCard>

      <div className="grid md:grid-cols-2 gap-5">
        <GlassCard>
          <div className="flex items-center mb-2">
            <div className="font-semibold text-sm">Assigned to me</div>
            <Link to="/officer/queue" className="ml-auto text-xs text-delft underline">full queue</Link>
          </div>
          {mine.length === 0 && <Empty msg="Nothing assigned to you right now." />}
          {mine.map((r) => (
            <Link key={r.id} to={`/officer/requests/${r.id}`} className="flex items-center gap-2 text-sm py-1.5">
              <SeverityBadge level={r.severity} size="sm" />
              <b className="font-mono">{r.code}</b>
              <span className="text-slate-500 ml-auto">{r.status.replace('_', ' ')}</span>
            </Link>
          ))}
        </GlassCard>
        <GlassCard>
          <div className="font-semibold text-sm mb-2">Pending review</div>
          {open.filter((r) => ['pending', 'under_review'].includes(r.status)).length === 0 && (
            <Empty msg="No requests awaiting review." />
          )}
          {open.filter((r) => ['pending', 'under_review'].includes(r.status)).slice(0, 6).map((r) => (
            <Link key={r.id} to={`/officer/requests/${r.id}`} className="flex items-center gap-2 text-sm py-1.5">
              <SeverityBadge level={r.severity} size="sm" />
              <b className="font-mono">{r.code}</b>
              <span className="text-slate-500 ml-auto">{r.status.replace('_', ' ')}</span>
            </Link>
          ))}
        </GlassCard>
      </div>
    </Stage>
  );
}
