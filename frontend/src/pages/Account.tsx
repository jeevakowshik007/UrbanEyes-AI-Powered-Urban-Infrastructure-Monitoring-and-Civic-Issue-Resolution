import { useEffect, useState } from 'react';
import api from '../services/api';
import { useAuth } from '../store/auth';
import { GlassCard, Stage } from '../components/ui';

export function Profile() {
  const { user } = useAuth();
  const [mine, setMine] = useState<any[]>([]);
  useEffect(() => {
    api.get('/api/v1/requests').then((r) => setMine(r.data.slice(0, 5))).catch(() => null);
  }, []);
  return (
    <Stage>
      <h1 className="font-display text-2xl font-bold">Profile</h1>
      <GlassCard>
        <div className="font-semibold">{user?.full_name}</div>
        <div className="text-sm text-slate-500">{user?.email} · role: {user?.role}</div>
        {user?.role === 'admin' && (
          <div className="text-sm mt-3">Your recent requests: {mine.length === 0 ? 'none yet' : mine.map((r) => r.code).join(', ')}</div>
        )}
      </GlassCard>
    </Stage>
  );
}

export function Settings() {
  const { user } = useAuth();
  const [health, setHealth] = useState<any>(null);
  useEffect(() => {
    api.get('/health').then((r) => setHealth(r.data)).catch(() => null);
  }, []);
  return (
    <Stage>
      <h1 className="font-display text-2xl font-bold">Settings</h1>
      <GlassCard>
        <div className="font-semibold text-sm mb-2">Account</div>
        <div className="text-sm text-slate-600">{user?.full_name} · {user?.email} · {user?.role}</div>
      </GlassCard>
      <GlassCard>
        <div className="font-semibold text-sm mb-2">Backend connection</div>
        <div className="text-sm text-slate-600">
          {health ? `API reachable · vision: ${health.cv_provider} · reasoning: ${health.reasoning_provider}` : 'API unreachable — is the backend running on :8000?'}
        </div>
        <div className="text-xs text-slate-400 mt-2">
          Sessions use short-lived JWT access tokens with rotating refresh tokens. Secrets live only in backend environment variables.
        </div>
      </GlassCard>
    </Stage>
  );
}
