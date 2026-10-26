import { GlassCard, SeverityBadge } from '../components/ui';

export interface Analysis {
  id: number;
  street_id: number;
  status: string;
  overall_severity?: string | null;
  weak_count: number;
  medium_count: number;
  critical_count: number;
  categories?: Record<string, string> | null;
  reason?: string | null;
  recommendation?: string | null;
  request_recommended?: boolean | null;
  reasoning_source: string;
  created_at: string;
}

const CAT_LABELS: Record<string, string> = {
  road_condition: 'Road Condition',
  waste_management: 'Waste Management',
  drainage: 'Drainage',
  street_infrastructure: 'Street Infrastructure',
};

export default function AnalysisCard({ a, action }: { a: Analysis; action?: React.ReactNode }) {
  const total = a.weak_count + a.medium_count + a.critical_count;
  return (
    <GlassCard>
      <div className="flex items-center gap-3 flex-wrap">
        <SeverityBadge level={a.overall_severity} />
        <span className="text-xs text-slate-500">
          {new Date(a.created_at).toLocaleString()} · source: UrbanEyes Infrastructure Reasoning
        </span>
        <span className="ml-auto">{action}</span>
      </div>

      {/* Severity distribution — counts of findings by level, never raw object counts */}
      <div className="grid grid-cols-3 gap-3 mt-4">
        {([['weak', a.weak_count, '#22a06b'], ['medium', a.medium_count, '#c9a227'], ['critical', a.critical_count, '#d64545']] as const).map(
          ([lvl, n, c]) => (
            <div key={lvl} className="rounded-xl bg-white/70 p-3 text-center shadow-sm">
              <div className="text-2xl font-display font-bold" style={{ color: c }}>{n}</div>
              <div className="text-[11px] uppercase tracking-wide text-slate-500">{lvl}</div>
            </div>
          ),
        )}
      </div>
      {total === 0 && <p className="text-sm text-slate-500 mt-3">No significant issues detected — street looks clear.</p>}

      {a.categories && (
        <div className="grid sm:grid-cols-2 gap-2 mt-4">
          {Object.entries(a.categories).map(([k, v]) => (
            <div key={k} className="flex items-center justify-between rounded-xl bg-white/70 px-3 py-2 text-sm shadow-sm">
              <span className="font-medium">{CAT_LABELS[k] ?? k}</span>
              <SeverityBadge level={v} size="sm" />
            </div>
          ))}
        </div>
      )}

      {a.reason && (
        <div className="mt-4 text-sm">
          <div className="font-semibold mb-1">AI explanation</div>
          <p className="text-slate-600 leading-relaxed">{a.reason}</p>
        </div>
      )}
      {a.recommendation && (
        <div className="mt-3 text-sm rounded-xl p-3" style={{ background: 'rgba(69,103,168,.08)' }}>
          <div className="font-semibold mb-1">Recommended municipal action</div>
          <p className="text-slate-600 leading-relaxed">{a.recommendation}</p>
        </div>
      )}
    </GlassCard>
  );
}

export function AnalysisSkeleton() {
  return (
    <GlassCard>
      <div className="animate-pulse space-y-3">
        <div className="h-6 w-32 bg-slate-200 rounded-full" />
        <div className="grid grid-cols-3 gap-3">
          <div className="h-16 bg-slate-100 rounded-xl" />
          <div className="h-16 bg-slate-100 rounded-xl" />
          <div className="h-16 bg-slate-100 rounded-xl" />
        </div>
        <div className="h-20 bg-slate-100 rounded-xl" />
      </div>
    </GlassCard>
  );
}
