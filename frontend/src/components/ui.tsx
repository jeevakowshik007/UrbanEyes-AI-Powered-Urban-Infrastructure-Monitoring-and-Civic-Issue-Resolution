import { ReactNode } from 'react';
import { motion } from 'framer-motion';
import { Link, useLocation, useNavigate } from 'react-router-dom';
import { useAuth, Role } from '../store/auth';

export const SEV_COLOR: Record<string, string> = {
  weak: '#22a06b',
  medium: '#c9a227',
  critical: '#d64545',
};

export function SeverityBadge({ level, size = 'md' }: { level?: string | null; size?: 'sm' | 'md' }) {
  if (!level) return <span className="text-slate-400 text-xs">not analyzed</span>;
  const c = SEV_COLOR[level] ?? '#888';
  return (
    <span
      className={`inline-flex items-center gap-1.5 font-semibold rounded-full text-white ${
        size === 'sm' ? 'text-[11px] px-2 py-0.5' : 'text-xs px-3 py-1'
      }`}
      style={{ background: `linear-gradient(135deg, ${c}, ${c}cc)`, boxShadow: `0 4px 12px ${c}55` }}
    >
      <span className="w-1.5 h-1.5 rounded-full bg-white/90" />
      {level.toUpperCase()}
    </span>
  );
}

export function GlassCard({ children, className = '' }: { children: ReactNode; className?: string }) {
  return (
    <motion.div
      initial={{ opacity: 0, y: 14 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.35 }}
      className={`glass rounded-2xl shadow-card p-5 ${className}`}
    >
      {children}
    </motion.div>
  );
}

export function Stage({ children }: { children: ReactNode }) {
  return <div className="max-w-7xl mx-auto px-4 md:px-6 py-6 space-y-5">{children}</div>;
}

const ADMIN_LINKS = [
  ['Dashboard', '/admin'],
  ['Streets', '/admin/streets'],
  ['History', '/admin/history'],
  ['Incidents', '/admin/incidents'],
  ['Requests', '/admin/requests'],
  ['Search', '/admin/search'],
  ['FAQ', '/admin/faq'],
  ['Settings', '/admin/settings'],
];

const OFFICER_LINKS = [
  ['Command', '/officer'],
  ['Queue', '/officer/queue'],
  ['Map', '/officer/map'],
  ['Search', '/officer/search'],
  ['FAQ', '/officer/faq'],
  ['Settings', '/officer/settings'],
];

export function Shell({ role, children }: { role: Role; children: ReactNode }) {
  const loc = useLocation();
  const nav = useNavigate();
  const { user, logout } = useAuth();
  const links = role === 'admin' ? ADMIN_LINKS : OFFICER_LINKS;
  return (
    <div className="min-h-screen">
      <header className="sticky top-0 z-30 glass border-b border-white/60">
        <div className="max-w-7xl mx-auto px-4 md:px-6 py-3 flex items-center gap-3">
          <div className="w-9 h-9 rounded-xl grid place-items-center text-white font-display font-extrabold shadow-float"
            style={{ background: 'linear-gradient(135deg,#7FBF9B,#4567A8)' }}>
            ◉
          </div>
          <div>
            <div className="font-display font-bold leading-none">UrbanEyes</div>
            <div className="text-[11px] text-slate-500">
              {role === 'admin' ? 'City Operations Command' : 'Field Response Console'}
            </div>
          </div>
          <nav className="ml-6 hidden lg:flex gap-1">
            {links.map(([label, to]) => (
              <Link
                key={to}
                to={to}
                className={`px-3 py-1.5 rounded-lg text-sm font-medium transition ${
                  loc.pathname === to ? 'bg-navy text-white shadow' : 'text-slate-600 hover:bg-white/70'
                }`}
              >
                {label}
              </Link>
            ))}
          </nav>
          <div className="ml-auto flex items-center gap-2">
            <Link to={role === 'admin' ? '/admin/notifications' : '/officer/notifications'}
              className="px-3 py-1.5 rounded-lg text-sm bg-white/70 hover:bg-white shadow-sm">🔔 Alerts</Link>
            <Link to={role === 'admin' ? '/admin/profile' : '/officer/profile'}
              className="px-3 py-1.5 rounded-lg text-sm bg-white/70 hover:bg-white shadow-sm hidden sm:block">
              {user?.full_name ?? 'Profile'}
            </Link>
            <button
              onClick={async () => { await logout(); nav('/login'); }}
              className="px-3 py-1.5 rounded-lg text-sm bg-navy text-white shadow"
            >
              Sign out
            </button>
          </div>
        </div>
        <nav className="lg:hidden flex gap-1 overflow-x-auto px-4 pb-2">
          {links.map(([label, to]) => (
            <Link key={to} to={to}
              className={`px-3 py-1.5 rounded-lg text-sm font-medium whitespace-nowrap ${
                loc.pathname === to ? 'bg-navy text-white' : 'bg-white/70 text-slate-600'
              }`}>
              {label}
            </Link>
          ))}
        </nav>
      </header>
      <main>{children}</main>
    </div>
  );
}

export function Empty({ msg }: { msg: string }) {
  return <div className="text-sm text-slate-500 bg-white/60 rounded-xl px-4 py-6 text-center">{msg}</div>;
}

export function Err({ msg }: { msg?: string | null }) {
  if (!msg) return null;
  return <div className="text-sm text-red-700 bg-red-50 border border-red-200 rounded-xl px-4 py-2">{msg}</div>;
}
