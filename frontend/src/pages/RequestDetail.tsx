import { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import api from '../services/api';
import { downloadFile } from '../services/download';
import AnalysisCard, { Analysis } from '../components/AnalysisCard';
import { GlassCard, SeverityBadge, Stage, Empty, Err } from '../components/ui';
import { useAuth } from '../store/auth';

const NEXT: Record<string, string[]> = {
  pending: ['under_review', 'accepted', 'rejected'],
  under_review: ['accepted', 'rejected'],
  accepted: ['assigned', 'rejected'],
  assigned: ['in_progress'],
  in_progress: ['resolved'],
  resolved: [],
  rejected: [],
};

export default function RequestDetail() {
  const { id } = useParams();
  const { user } = useAuth();
  const [req, setReq] = useState<any>(null);
  const [analysis, setAnalysis] = useState<Analysis | null>(null);
  const [history, setHistory] = useState<any[]>([]);
  const [evidence, setEvidence] = useState<any[]>([]);
  const [reason, setReason] = useState('');
  const [officerId, setOfficerId] = useState('');
  const [err, setErr] = useState<string | null>(null);
  const [busy, setBusy] = useState(false);

  async function refresh() {
    const r = await api.get(`/api/v1/requests/${id}`);
    setReq(r.data);
    const a = await api.get(`/api/v1/analyses/${r.data.analysis_id}`).catch(() => null);
    if (a) setAnalysis(a.data);
    const h = await api.get(`/api/v1/requests/${id}/history`).catch(() => ({ data: [] }));
    setHistory(h.data);
    const e = await api.get(`/api/v1/requests/${id}/evidence`).catch(() => ({ data: [] }));
    setEvidence(e.data);
  }

  useEffect(() => { refresh().catch(console.error); /* eslint-disable-next-line */ }, [id]);

  async function act(to: string) {
    setBusy(true); setErr(null);
    try {
      await api.patch(`/api/v1/requests/${id}/status`, { to_status: to, reason: reason || undefined });
      setReason('');
      await refresh();
    } catch (ex: any) {
      setErr(ex.response?.data?.detail ?? 'Transition failed');
    } finally { setBusy(false); }
  }

  async function assign() {
    setBusy(true); setErr(null);
    try {
      await api.post(`/api/v1/requests/${id}/assignments`, { officer_id: Number(officerId) });
      setOfficerId('');
      await refresh();
    } catch (ex: any) {
      setErr(ex.response?.data?.detail ?? 'Assignment failed');
    } finally { setBusy(false); }
  }

  async function upload(kind: string, file: File, notes?: string) {
    setBusy(true); setErr(null);
    try {
      const fd = new FormData();
      fd.append('file', file);
      await api.post(`/api/v1/requests/${id}/evidence?kind=${kind}`, fd);
      const e = await api.get(`/api/v1/requests/${id}/evidence`).catch(() => ({ data: [] }));
      setEvidence(e.data);
    } catch (ex: any) {
      setErr(ex.response?.data?.detail ?? 'Evidence upload failed');
    } finally { setBusy(false); }
  }

  if (!req) return <Stage><Empty msg="Loading request…" /></Stage>;
  const isOfficer = user?.role === 'officer';

  return (
    <Stage>
      <div className="flex items-center gap-3 flex-wrap">
        <h1 className="font-display text-2xl font-bold font-mono">{req.code}</h1>
        <SeverityBadge level={req.severity} />
        <span className="text-xs px-3 py-1 rounded-full bg-delft text-white font-semibold">
          {req.status.replace('_', ' ').toUpperCase()}
        </span>
      </div>
      <Err msg={err} />

      {analysis && <AnalysisCard a={analysis} />}

      <div className="grid md:grid-cols-2 gap-5">
        <GlassCard>
          <div className="font-semibold text-sm mb-3">Status history (auditable)</div>
          <ol className="relative border-l-2 border-delft/20 ml-2 space-y-3">
            {history.map((h) => (
              <li key={h.id} className="ml-4 text-sm">
                <span className="absolute -left-[7px] mt-1 w-3 h-3 rounded-full bg-delft" />
                <b>{h.from_status ?? '—'} → {h.to_status}</b>
                <span className="text-slate-500"> · {new Date(h.created_at).toLocaleString()}</span>
                {h.reason && <div className="text-slate-600">{h.reason}</div>}
              </li>
            ))}
          </ol>
        </GlassCard>

        <div className="space-y-5">
          {isOfficer ? (
            <GlassCard>
              <div className="font-semibold text-sm mb-3">Officer actions</div>
              <div className="flex gap-2 flex-wrap">
                {(NEXT[req.status] ?? []).filter((s) => s !== 'assigned').map((s) => (
                  <button key={s} disabled={busy} onClick={() => act(s)}
                    className={`px-4 py-2 rounded-xl text-sm font-semibold text-white shadow disabled:opacity-50 ${
                      s === 'rejected' ? 'bg-slate-500' : s === 'resolved' ? 'bg-weak' : 'bg-delft'
                    }`}>
                    {s === 'resolved' ? 'Mark resolved' : s.replace('_', ' ')}
                  </button>
                ))}
              </div>
              {(NEXT[req.status] ?? []).includes('assigned') && (
                <div className="flex gap-2 mt-3">
                  <input value={officerId} onChange={(e) => setOfficerId(e.target.value)} placeholder="Officer user ID"
                    className="flex-1 px-3 py-2 rounded-xl border border-slate-200 bg-white/80 text-sm" />
                  <button disabled={busy} onClick={assign} className="px-4 py-2 rounded-xl bg-delft text-white text-sm font-semibold">
                    Assign
                  </button>
                </div>
              )}
              <input value={reason} onChange={(e) => setReason(e.target.value)}
                placeholder="Reason (required to reject)"
                className="w-full mt-3 px-3 py-2 rounded-xl border border-slate-200 bg-white/80 text-sm" />
              <div className="mt-4">
                <div className="text-sm font-semibold mb-2">Resolution evidence (required before resolving)</div>
                {(['before', 'after', 'repair'] as const).map((k) => (
                  <label key={k} className="block mt-2 px-3 py-2 rounded-xl bg-white/70 text-sm cursor-pointer hover:bg-white shadow-sm">
                    Upload {k} image
                    <input type="file" accept="image/*" className="hidden"
                      onChange={(e) => e.target.files?.[0] && upload(k, e.target.files[0])} />
                  </label>
                ))}
                {evidence.length === 0 && (
                  <div className="text-xs text-slate-500 mt-1">No evidence uploaded yet.</div>
                )}
                {evidence.map((e) => (
                  <div key={e.id} className="flex items-center gap-2 text-xs text-slate-600 mt-1 rounded-lg bg-white/70 px-2 py-1.5">
                    <span>✓ {e.kind} · {new Date(e.created_at).toLocaleString()}</span>
                    <button onClick={() => downloadFile(e.storage_key).catch(() => setErr('Download failed'))}
                      className="ml-auto text-delft underline font-semibold">Download</button>
                  </div>
                ))}
              </div>
            </GlassCard>
          ) : (
            <GlassCard>
              <div className="font-semibold text-sm mb-2">Tracking</div>
              <p className="text-sm text-slate-600">
                Submitted by admin #{req.submitted_by} · {new Date(req.created_at).toLocaleString()}
                {req.note && <><br />Note: “{req.note}”</>}
              </p>
              <p className="text-xs text-slate-400 mt-2">
                The officer will accept, assign, work, upload repair evidence, then resolve. Every step appears in the history.
              </p>
            </GlassCard>
          )}
        </div>
      </div>
    </Stage>
  );
}
