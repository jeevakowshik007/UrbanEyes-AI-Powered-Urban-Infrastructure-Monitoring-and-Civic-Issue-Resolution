import { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import api from '../services/api';
import { GlassCard, SeverityBadge, Stage, Empty } from '../components/ui';

export default function Incidents({ base }: { base: string }) {
  const [items, setItems] = useState<any[]>([]);
  const [filter, setFilter] = useState('');
  useEffect(() => {
    api.get(`/api/v1/incidents${filter ? `?severity=${filter}` : ''}`)
      .then((r) => setItems(r.data)).catch(console.error);
  }, [filter]);
  return (
    <Stage>
      <div className="flex items-center gap-2">
        <h1 className="font-display text-2xl font-bold">Incidents</h1>
        <span className="ml-auto flex gap-2">
          {['', 'critical', 'medium', 'weak'].map((f) => (
            <button key={f} onClick={() => setFilter(f)}
              className={`px-3 py-1.5 rounded-lg text-xs font-semibold ${filter === f ? 'bg-navy text-white' : 'bg-white/70'}`}>
              {f || 'all'}
            </button>
          ))}
        </span>
      </div>
      {items.length === 0 && <Empty msg="No incidents at this severity." />}
      <div className="grid md:grid-cols-2 gap-4">
        {items.map((i) => (
          <GlassCard key={i.id}>
            <div className="flex items-center gap-2">
              <SeverityBadge level={i.severity} />
              <span className="text-sm font-semibold">Incident #{i.id}</span>
              <span className="ml-auto text-xs text-slate-400">{i.status}</span>
            </div>
            <div className="text-sm text-slate-500 mt-2">
              Street {i.street_id} · {new Date(i.created_at).toLocaleString()}
            </div>
            <Link to={`${base}/streets?street=${i.street_id}`} className="text-sm text-delft underline">
              Open street analysis →
            </Link>
          </GlassCard>
        ))}
      </div>
    </Stage>
  );
}
