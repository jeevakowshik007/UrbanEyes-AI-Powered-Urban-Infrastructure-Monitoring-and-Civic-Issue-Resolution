import { useEffect, useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer, PieChart, Pie, Cell } from 'recharts';
import api from '../../services/api';
import UrbanOpsMap, { MapPoint } from '../../components/UrbanOpsMap';
import ProviderBadge from '../../components/ProviderBadge';
import { GlassCard, SeverityBadge, Stage, Empty } from '../../components/ui';

interface Street {
  id: number; name: string; area: string; latitude: number; longitude: number;
  video_count: number; latest_severity?: string | null; latest_analysis_at?: string | null;
}

export default function AdminDashboard() {
  const nav = useNavigate();
  const [streets, setStreets] = useState<Street[]>([]);
  const [dash, setDash] = useState<any>(null);
  const [recent, setRecent] = useState<any[]>([]);
  const [notes, setNotes] = useState<any[]>([]);

  useEffect(() => {
    (async () => {
      const [s, d, r, n] = await Promise.all([
        api.get('/api/v1/streets'),
        api.get('/api/v1/dashboard'),
        api.get('/api/v1/analyses'),
        api.get('/api/v1/notifications?unread_only=true'),
      ]);
      setStreets(s.data);
      setDash(d.data);
      setRecent(r.data.slice(0, 5));
      setNotes(n.data.slice(0, 5));
    })().catch(console.error);
  }, []);

  const points: MapPoint[] = streets.map((s) => ({
    id: s.id, lat: s.latitude, lon: s.longitude, severity: s.latest_severity,
    label: `${s.name} — ${s.latest_severity ?? 'not analyzed'}`, kind: 'street',
  }));
  const critical = streets.filter((s) => s.latest_severity === 'critical');

  const statusData = dash ? Object.entries(dash.requests_by_status).map(([k, v]) => ({ name: k, value: v as number })) : [];
  const sevData = ['weak', 'medium', 'critical'].map((lvl) => ({
    name: lvl, streets: streets.filter((s) => s.latest_severity === lvl).length,
  }));

  return (
    <Stage>
      <ProviderBadge />
      <div className="flex items-end flex-wrap gap-3">
        <div>
          <h1 className="font-display text-2xl font-bold">City Operations Command</h1>
          <p className="text-sm text-slate-500">
            {streets.length} monitored streets · {dash?.critical_analyses ?? 0} critical analyses ·{' '}
            {dash?.open_requests ?? 0} open requests
          </p>
        </div>
        {critical.length > 0 && (
          <button onClick={() => nav('/admin/incidents')}
            className="ml-auto px-4 py-2 rounded-xl text-white text-sm font-semibold shadow-float animate-pulse"
            style={{ background: 'linear-gradient(135deg,#d64545,#a82e2e)' }}>
            ⚠ {critical.length} critical street{critical.length > 1 ? 's' : ''} need review
          </button>
        )}
      </div>

      <GlassCard>
        <div className="font-semibold mb-3">Monitored area — select a street to analyze</div>
        <UrbanOpsMap points={points} onSelect={(p) => nav(`/admin/streets?street=${p.id}`)} />
        <div className="flex gap-2 mt-3 flex-wrap">
          {streets.map((s) => (
            <button key={s.id} onClick={() => nav(`/admin/streets?street=${s.id}`)}
              className="flex items-center gap-2 px-3 py-1.5 rounded-xl bg-white/70 hover:bg-white text-sm shadow-sm">
              <span className="w-2.5 h-2.5 rounded-full"
                style={{ background: s.latest_severity === 'critical' ? '#d64545' : s.latest_severity === 'medium' ? '#c9a227' : s.latest_severity === 'weak' ? '#22a06b' : '#cbd5e1' }} />
              {s.name}
            </button>
          ))}
        </div>
      </GlassCard>

      <div className="grid md:grid-cols-3 gap-5">
        <GlassCard>
          <div className="font-semibold text-sm mb-2">Request pipeline — where is work stuck?</div>
          {statusData.every((d) => d.value === 0) ? <Empty msg="No municipal requests yet." /> : (
            <ResponsiveContainer width="100%" height={200}>
              <BarChart data={statusData} layout="vertical">
                <XAxis type="number" hide />
                <YAxis type="category" dataKey="name" width={90} tick={{ fontSize: 11 }} />
                <Tooltip />
                <Bar dataKey="value" fill="#4567A8" radius={[0, 6, 6, 0]} />
              </BarChart>
            </ResponsiveContainer>
          )}
        </GlassCard>
        <GlassCard>
          <div className="font-semibold text-sm mb-2">Street health by severity</div>
          <ResponsiveContainer width="100%" height={200}>
            <PieChart>
              <Pie data={sevData} dataKey="streets" nameKey="name" innerRadius={45} outerRadius={75} paddingAngle={3}>
                {sevData.map((e) => (
                  <Cell key={e.name} fill={e.name === 'critical' ? '#d64545' : e.name === 'medium' ? '#D8C46A' : '#7FBF9B'} />
                ))}
              </Pie>
              <Tooltip />
            </PieChart>
          </ResponsiveContainer>
        </GlassCard>
        <GlassCard>
          <div className="font-semibold text-sm mb-2">Needs attention</div>
          <div className="space-y-2">
            {notes.length === 0 && <Empty msg="All clear — no unread alerts." />}
            {notes.map((n) => (
              <Link key={n.id} to="/admin/notifications" className="block text-sm rounded-xl bg-white/70 px-3 py-2 hover:bg-white shadow-sm">
                <span className="font-semibold">{n.title}</span>
                <span className="text-slate-500"> — {new Date(n.created_at).toLocaleString()}</span>
              </Link>
            ))}
          </div>
        </GlassCard>
      </div>

      <GlassCard>
        <div className="flex items-center mb-3">
          <div className="font-semibold text-sm">Recent analyses</div>
          <Link to="/admin/history" className="ml-auto text-sm text-delft underline">full history</Link>
        </div>
        <div className="space-y-2">
          {recent.length === 0 && <Empty msg="No analyses yet — pick a street to run the first one." />}
          {recent.map((a) => (
            <div key={a.id} className="flex items-center gap-3 text-sm rounded-xl bg-white/70 px-3 py-2 shadow-sm">
              <SeverityBadge level={a.overall_severity} size="sm" />
              <span>Analysis #{a.id} · street {a.street_id}</span>
              <span className="text-slate-400 ml-auto">{new Date(a.created_at).toLocaleString()}</span>
            </div>
          ))}
        </div>
      </GlassCard>
    </Stage>
  );
}
