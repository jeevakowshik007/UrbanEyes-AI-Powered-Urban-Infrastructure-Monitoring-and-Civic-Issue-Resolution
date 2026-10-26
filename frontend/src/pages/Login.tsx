import { useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import { useAuth, Role } from '../store/auth';
import { Err } from '../components/ui';

export default function Login() {
  const nav = useNavigate();
  const { login, register } = useAuth();
  const [mode, setMode] = useState<'login' | 'register'>('login');
  const [email, setEmail] = useState('admin@urbaneyes.city');
  const [password, setPassword] = useState('Admin123!');
  const [name, setName] = useState('City Administrator');
  const [role, setRole] = useState<Role>('admin');
  const [err, setErr] = useState<string | null>(null);
  const [busy, setBusy] = useState(false);

  async function submit(e: React.FormEvent) {
    e.preventDefault();
    setBusy(true);
    setErr(null);
    try {
      const r = mode === 'login'
        ? await login(email, password)
        : await register(email, password, name, role);
      nav(r === 'admin' ? '/admin' : '/officer');
    } catch (ex: any) {
      setErr(ex.response?.data?.detail ?? 'Authentication failed');
    } finally {
      setBusy(false);
    }
  }

  return (
    <div className="min-h-screen grid place-items-center px-4">
      <div className="glass rounded-3xl shadow-float p-8 w-full max-w-md">
        <div className="w-12 h-12 rounded-2xl grid place-items-center text-white text-xl font-bold mb-4"
          style={{ background: 'linear-gradient(135deg,#7FBF9B,#4567A8)' }}>◉</div>
        <h1 className="font-display text-2xl font-bold">UrbanEyes</h1>
        <p className="text-sm text-slate-500 mb-6">Observe → Analyze → Understand → Prioritize → Request → Act → Verify → Resolve</p>
        <div className="flex gap-2 mb-5">
          {(['login', 'register'] as const).map((m) => (
            <button key={m} onClick={() => setMode(m)}
              className={`px-4 py-1.5 rounded-lg text-sm font-semibold ${mode === m ? 'bg-navy text-white' : 'bg-white/70 text-slate-600'}`}>
              {m === 'login' ? 'Sign in' : 'Register'}
            </button>
          ))}
        </div>
        <form onSubmit={submit} className="space-y-3">
          {mode === 'register' && (
            <>
              <input className="w-full px-3 py-2 rounded-xl border border-slate-200 bg-white/80" placeholder="Full name"
                value={name} onChange={(e) => setName(e.target.value)} required />
              <div className="flex gap-2">
                {(['admin', 'officer'] as Role[]).map((r) => (
                  <button type="button" key={r} onClick={() => setRole(r)}
                    className={`flex-1 px-3 py-2 rounded-xl text-sm font-semibold ${role === r ? 'bg-delft text-white' : 'bg-white/70 text-slate-600'}`}>
                    {r === 'admin' ? 'Administrator' : 'Municipal Officer'}
                  </button>
                ))}
              </div>
            </>
          )}
          <input className="w-full px-3 py-2 rounded-xl border border-slate-200 bg-white/80" placeholder="Email"
            type="email" value={email} onChange={(e) => setEmail(e.target.value)} required />
          <input className="w-full px-3 py-2 rounded-xl border border-slate-200 bg-white/80" placeholder="Password"
            type="password" value={password} onChange={(e) => setPassword(e.target.value)} required />
          <Err msg={err} />
          <button disabled={busy}
            className="w-full py-2.5 rounded-xl text-white font-semibold shadow-float disabled:opacity-60"
            style={{ background: 'linear-gradient(135deg,#5DA87F,#4567A8)' }}>
            {busy ? 'Please wait…' : mode === 'login' ? 'Sign in to command center' : 'Create account'}
          </button>
        </form>
        <p className="text-xs text-slate-500 mt-4">
          Demo: admin@urbaneyes.city / Admin123! · officer@urbaneyes.city / Officer123!
        </p>
        <Link to="/faq" className="text-xs text-delft underline">What is UrbanEyes?</Link>
      </div>
    </div>
  );
}
