import { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import api from '../services/api';
import { GlassCard, SeverityBadge, Stage, Empty } from '../components/ui';

const STATUSES = ['', 'pending', 'under_review', 'accepted', 'assigned', 'in_progress', 'resolved', 'rejected'];

export default function Requests({ base, mineToggle }: { base: string; mineToggle?: boolean }) {
  const [items, setItems] = useState<any[]>([]);
  const [status, setStatus] = useState('');
  const [mine, setMine] = useState(false);

  useEffect(() => {
    const q = new URLSearchParams();
    if (status) q.set('status', status);
    if (mine) q.set('mine', 'true');
    api.get(`/api/v1/requests?${q}`).then((r) => setItems(r.data)).catch(console.error);
  }, [status, mine]);

  return (
    <Stage>
      <div className="flex items-center gap-2 flex-wrap">
        <h1 className="font-display text-2xl font-bold">Municipal Requests</h1>
        {mineToggle && (
          <button onClick={() => setMine(!mine)}
            className={`ml-auto px-3 py-1.5 rounded-lg text-xs font-semibold ${mine ? 'bg-delft text-white' : 'bg-white/70'}`}>
            {mine ? 'Assigned to me ✓' : 'Assigned to me'}
          </button>
        )}
      </div>
      <div className="flex gap-2 flex-wrap">
        {STATUSES.map((s) => (
          <button key={s} onClick={() => setStatus(s)}
            className={`px-3 py-1.5 rounded-lg text-xs font-semibold ${status === s ? 'bg-navy text-white' : 'bg-white/70'}`}>
            {s || 'all'}
          </button>
        ))}
      </div>
      {items.length === 0 && <Empty msg="No requests in this view." />}
      <div className="grid md:grid-cols-2 gap-4">
        {items.map((r) => (
          <Link key={r.id} to={`${base}/requests/${r.id}`}>
            <GlassCard className="hover:shadow-float transition">
              <div className="flex items-center gap-2">
                <SeverityBadge level={r.severity} size="sm" />
                <span className="font-mono font-bold text-sm">{r.code}</span>
                <span className="ml-auto text-xs px-2 py-0.5 rounded-full bg-delft/10 text-delft font-semibold">
                  {r.status.replace('_', ' ')}
                </span>
              </div>
              <div className="text-xs text-slate-500 mt-2">
                Street {r.street_id} · {new Date(r.created_at).toLocaleString()}
              </div>
            </GlassCard>
          </Link>
        ))}
      </div>
    </Stage>
  );
}
