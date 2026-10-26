import { useEffect, useState } from 'react';
import api from '../../services/api';
import AnalysisCard, { Analysis, AnalysisSkeleton } from '../../components/AnalysisCard';
import { GlassCard, Stage, Empty } from '../../components/ui';

export default function History() {
  const [items, setItems] = useState<Analysis[] | null>(null);
  useEffect(() => {
    api.get('/api/v1/analyses').then((r) => setItems(r.data)).catch(() => setItems([]));
  }, []);
  return (
    <Stage>
      <h1 className="font-display text-2xl font-bold">Analysis History</h1>
      {!items && <AnalysisSkeleton />}
      {items?.length === 0 && <Empty msg="No analyses recorded yet." />}
      <div className="space-y-4">
        {items?.map((a) => a.status === 'done' ? <AnalysisCard key={a.id} a={a} /> : (
          <GlassCard key={a.id}>
            <div className="text-sm">Analysis #{a.id} — status: <b>{a.status}</b></div>
          </GlassCard>
        ))}
      </div>
    </Stage>
  );
}
