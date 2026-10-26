import { useEffect, useState } from 'react';
import api from '../services/api';
import { GlassCard, Stage, Empty } from '../components/ui';

export default function Notifications() {
  const [items, setItems] = useState<any[]>([]);
  useEffect(() => {
    api.get('/api/v1/notifications').then((r) => setItems(r.data)).catch(console.error);
  }, []);
  async function mark(id: number) {
    await api.patch(`/api/v1/notifications/${id}/read`).catch(() => null);
    setItems((xs) => xs.map((x) => (x.id === id ? { ...x, is_read: true } : x)));
  }
  return (
    <Stage>
      <h1 className="font-display text-2xl font-bold">Notifications</h1>
      {items.length === 0 && <Empty msg="No notifications." />}
      <div className="space-y-2">
        {items.map((n) => (
          <GlassCard key={n.id} className={n.is_read ? 'opacity-70' : ''}>
            <div className="flex items-center gap-2">
              <span className={`w-2 h-2 rounded-full ${n.is_read ? 'bg-slate-300' : 'bg-critical'}`} />
              <span className="font-semibold text-sm">{n.title}</span>
              <span className="ml-auto text-xs text-slate-400">{new Date(n.created_at).toLocaleString()}</span>
            </div>
            <p className="text-sm text-slate-600 mt-1">{n.body}</p>
            {!n.is_read && (
              <button onClick={() => mark(n.id)} className="mt-2 text-xs text-delft underline">Mark read</button>
            )}
          </GlassCard>
        ))}
      </div>
    </Stage>
  );
}
