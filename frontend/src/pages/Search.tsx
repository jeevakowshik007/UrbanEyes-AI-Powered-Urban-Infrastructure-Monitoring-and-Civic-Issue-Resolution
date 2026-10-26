import { useState } from 'react';
import { Link } from 'react-router-dom';
import api from '../services/api';
import { GlassCard, Stage, Err } from '../components/ui';

export default function Search({ base }: { base: string }) {
  const [q, setQ] = useState('');
  const [res, setRes] = useState<any>(null);
  const [err, setErr] = useState<string | null>(null);
  async function go(e: React.FormEvent) {
    e.preventDefault();
    setErr(null);
    try {
      const { data } = await api.get(`/api/v1/search?q=${encodeURIComponent(q)}`);
      setRes(data);
    } catch (ex: any) {
      setErr(ex.response?.data?.detail ?? 'Search failed');
    }
  }
  return (
    <Stage>
      <h1 className="font-display text-2xl font-bold">Search</h1>
      <form onSubmit={go} className="flex gap-2">
        <input value={q} onChange={(e) => setQ(e.target.value)} placeholder="Street name, area, or request code (UE-…)"
          className="flex-1 px-4 py-2.5 rounded-xl border border-slate-200 bg-white/80" />
        <button className="px-5 py-2.5 rounded-xl bg-navy text-white text-sm font-semibold">Search</button>
      </form>
      <Err msg={err} />
      {res && (
        <div className="grid md:grid-cols-2 gap-4">
          <GlassCard>
            <div className="font-semibold text-sm mb-2">Streets</div>
            {res.streets.map((s: any) => (
              <Link key={s.id} to={`${base}/streets?street=${s.id}`} className="block text-sm py-1 text-delft underline">
                {s.name} · {s.area}
              </Link>
            ))}
            {res.streets.length === 0 && <div className="text-sm text-slate-500">No streets match.</div>}
          </GlassCard>
          <GlassCard>
            <div className="font-semibold text-sm mb-2">Requests</div>
            {res.requests.map((r: any) => (
              <Link key={r.id} to={`${base}/requests/${r.id}`} className="block text-sm py-1 text-delft underline">
                {r.code} · {r.status}
              </Link>
            ))}
            {res.requests.length === 0 && <div className="text-sm text-slate-500">No requests match.</div>}
          </GlassCard>
        </div>
      )}
    </Stage>
  );
}
