import { useCallback, useEffect, useRef, useState } from 'react';
import { useSearchParams, useNavigate } from 'react-router-dom';
import { LineChart, Line, XAxis, YAxis, Tooltip, ResponsiveContainer } from 'recharts';
import api from '../../services/api';
import { downloadFile } from '../../services/download';
import AnalysisCard, { Analysis } from '../../components/AnalysisCard';
import UrbanOpsMap, { MapPoint } from '../../components/UrbanOpsMap';
import { GlassCard, SeverityBadge, Stage, Empty, Err } from '../../components/ui';

interface Street {
  id: number; name: string; area: string; latitude: number; longitude: number;
  video_count: number; latest_severity?: string | null;
}

export default function StreetAnalysis() {
  const [params] = useSearchParams();
  const nav = useNavigate();
  const [streets, setStreets] = useState<Street[]>([]);
  const [sid, setSid] = useState<number | null>(params.get('street') ? Number(params.get('street')) : null);
  const [videos, setVideos] = useState<any[]>([]);
  const [analyses, setAnalyses] = useState<Analysis[]>([]);
  const [busy, setBusy] = useState(false);
  const [err, setErr] = useState<string | null>(null);
  const [confirm, setConfirm] = useState<Analysis | null>(null);
  const [note, setNote] = useState('');
  const pollRef = useRef<number | null>(null);

  const load = useCallback(async (id: number) => {
    const [v, a] = await Promise.all([
      api.get(`/api/v1/videos?street_id=${id}`),
      api.get(`/api/v1/analyses?street_id=${id}`),
    ]);
    setVideos(v.data);
    setAnalyses(a.data);
  }, []);

  useEffect(() => {
    api.get('/api/v1/streets').then((r) => {
      setStreets(r.data);
      const initial = sid ?? r.data[0]?.id ?? null;
      if (initial) { setSid(initial); load(initial).catch(console.error); }
    }).catch(console.error);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  useEffect(() => () => { if (pollRef.current) window.clearInterval(pollRef.current); }, []);

  const street = streets.find((s) => s.id === sid);

  async function runAnalysis() {
    if (!sid) return;
    setBusy(true); setErr(null);
    try {
      const { data } = await api.post('/api/v1/analyses', { street_id: sid });
      pollRef.current = window.setInterval(async () => {
        try {
          const a = (await api.get(`/api/v1/analyses/${data.analysis_id}`)).data as Analysis;
          if (a.status === 'done' || a.status === 'failed') {
            if (pollRef.current) window.clearInterval(pollRef.current);
            if (a.status === 'failed') setErr('Analysis failed — check video and retry.');
            await load(sid);
            setBusy(false); // clear only after fresh results land — never act on stale data
          }
        } catch { /* keep polling */ }
      }, 1500);
    } catch (ex: any) {
      setBusy(false);
      setErr(ex.response?.data?.detail ?? 'Could not start analysis');
    }
  }

  async function uploadVideo(file: File) {
    if (!sid) return;
    setErr(null);
    try {
      const fd = new FormData();
      fd.append('file', file);
      await api.post(`/api/v1/videos/upload?street_id=${sid}`, fd);
      await load(sid);
    } catch (ex: any) {
      setErr(ex.response?.data?.detail ?? 'Upload failed');
    }
  }

  async function submitRequest() {
    if (!confirm) return;
    setErr(null);
    try {
      const { data } = await api.post('/api/v1/requests', { analysis_id: confirm.id, note: note || undefined });
      setConfirm(null);
      setNote('');
      nav(`/admin/requests/${data.id}`);
    } catch (ex: any) {
      setErr(ex.response?.data?.detail ?? 'Could not submit request');
    }
  }

  const latest = analyses[0];
  const trend = [...analyses].reverse().map((a) => ({
    t: new Date(a.created_at).toLocaleDateString(),
    weak: a.weak_count, medium: a.medium_count, critical: a.critical_count,
  }));

  return (
    <Stage>
      <h1 className="font-display text-2xl font-bold">Street Analysis</h1>
      <div className="flex gap-2 flex-wrap">
        {streets.map((s) => (
          <button key={s.id} onClick={() => { setSid(s.id); setErr(null); load(s.id).catch(console.error); }}
            className={`px-4 py-2 rounded-xl text-sm font-semibold shadow-sm ${sid === s.id ? 'bg-navy text-white' : 'bg-white/70 hover:bg-white'}`}>
            {s.name}
          </button>
        ))}
      </div>

      {streets.length > 0 && (
        <div>
          <div className="text-xs text-slate-500 mb-1">
            Pick a street — click its pin (or anywhere up to 1.5 km from one), then run the analysis below.
          </div>
          <UrbanOpsMap
            points={streets.map((s) => ({
              id: s.id, lat: s.latitude, lon: s.longitude,
              severity: s.latest_severity, label: `${s.name} — ${s.area}`, kind: 'street' as const,
            }))}
            onSelect={(p) => { setSid(p.id); setErr(null); load(p.id).catch(console.error); }}
            height={340}
          />
        </div>
      )}

      {street && (
        <GlassCard>
          <div className="flex items-center gap-3 flex-wrap">
            <div>
              <div className="font-display font-bold text-lg">{street.name}</div>
              <div className="text-xs text-slate-500">{street.area} · {street.latitude.toFixed(4)}, {street.longitude.toFixed(4)}</div>
            </div>
            <span className="ml-auto flex items-center gap-2">
              <SeverityBadge level={street.latest_severity} />
            </span>
          </div>
          <div className="mt-3 text-sm space-y-1">
            {videos.length === 0 && 'No recorded video for this street yet — upload one to enable analysis.'}
            {videos.map((v: any) => (
              <div key={v.id} className="flex items-center gap-2 rounded-lg bg-white/70 px-3 py-1.5 shadow-sm">
                <span>🎬 {v.filename} · {(v.size_bytes / 1048576).toFixed(1)} MB · {v.status}</span>
                <button onClick={() => downloadFile(v.storage_key).catch(() => setErr('Download failed'))}
                  className="ml-auto text-delft underline font-semibold">Download</button>
              </div>
            ))}
          </div>
          <div className="flex gap-2 mt-3 flex-wrap">
            <label className="px-4 py-2 rounded-xl bg-white/80 hover:bg-white text-sm font-semibold shadow-sm cursor-pointer">
              Upload street video
              <input type="file" accept="video/*" className="hidden"
                onChange={(e) => e.target.files?.[0] && uploadVideo(e.target.files[0])} />
            </label>
            <button onClick={runAnalysis} disabled={busy || videos.length === 0}
              className="px-4 py-2 rounded-xl text-white text-sm font-semibold shadow-float disabled:opacity-50"
              style={{ background: 'linear-gradient(135deg,#5DA87F,#4567A8)' }}>
              {busy ? 'Analyzing… (YOLO + local reasoning)' : 'Run street analysis'}
            </button>
          </div>
          <Err msg={err} />
        </GlassCard>
      )}

      {busy && <div className="text-sm text-slate-500">Pipeline running: validate → frames → YOLO26-Seg → severity → local infrastructure reasoning…</div>}

      {latest && latest.status === 'done' && (
        <AnalysisCard
          a={latest}
          action={
            <button onClick={() => setConfirm(latest)}
              className="px-4 py-2 rounded-xl text-white text-sm font-semibold shadow-float"
              style={{ background: latest.overall_severity === 'critical' ? 'linear-gradient(135deg,#d64545,#a82e2e)' : 'linear-gradient(135deg,#4567A8,#33497e)' }}>
              Submit Municipal Request
            </button>
          }
        />
      )}

      {analyses.length > 1 && (
        <GlassCard>
          <div className="font-semibold text-sm mb-2">Severity trend — is this street getting worse?</div>
          <ResponsiveContainer width="100%" height={180}>
            <LineChart data={trend}>
              <XAxis dataKey="t" tick={{ fontSize: 11 }} />
              <YAxis allowDecimals={false} tick={{ fontSize: 11 }} />
              <Tooltip />
              <Line type="monotone" dataKey="critical" stroke="#d64545" strokeWidth={2} dot={false} />
              <Line type="monotone" dataKey="medium" stroke="#c9a227" strokeWidth={2} dot={false} />
              <Line type="monotone" dataKey="weak" stroke="#22a06b" strokeWidth={2} dot={false} />
            </LineChart>
          </ResponsiveContainer>
        </GlassCard>
      )}

      {analyses.length === 0 && street && <Empty msg="No analyses for this street yet." />}

      {confirm && (
        <div className="fixed inset-0 z-50 grid place-items-center bg-navy/40 p-4" onClick={() => setConfirm(null)}>
          <div className="glass rounded-2xl shadow-float p-6 w-full max-w-lg" onClick={(e) => e.stopPropagation()}>
            <h2 className="font-display font-bold text-lg">Confirm municipal request</h2>
            <p className="text-sm text-slate-600 mt-2">
              {confirm.overall_severity === 'critical'
                ? 'This analysis is CRITICAL. Nothing is submitted automatically — review the evidence above and confirm explicitly.'
                : 'Review the analysis above. Submitting notifies the municipal officer queue.'}
            </p>
            <div className="flex gap-3 mt-3 text-sm">
              <span>Weak <b>{confirm.weak_count}</b></span>
              <span>Medium <b>{confirm.medium_count}</b></span>
              <span>Critical <b>{confirm.critical_count}</b></span>
            </div>
            <textarea value={note} onChange={(e) => setNote(e.target.value)} placeholder="Note for the officer (optional)"
              className="w-full mt-3 px-3 py-2 rounded-xl border border-slate-200 bg-white/80 text-sm" rows={3} />
            <div className="flex gap-2 mt-4">
              <button onClick={() => setConfirm(null)} className="flex-1 py-2 rounded-xl bg-white/80 text-sm font-semibold">Cancel</button>
              <button onClick={submitRequest} className="flex-1 py-2 rounded-xl text-white text-sm font-semibold"
                style={{ background: 'linear-gradient(135deg,#d64545,#a82e2e)' }}>
                Confirm & submit request
              </button>
            </div>
          </div>
        </div>
      )}
    </Stage>
  );
}
