import { useEffect, useState } from 'react';
import { BrowserRouter, Routes, Route, Navigate, Outlet } from 'react-router-dom';
import { useAuth, Role } from './store/auth';
import { Shell, Stage } from './components/ui';
import api from './services/api';
import Login from './pages/Login';
import Faq from './pages/Faq';
import AdminDashboard from './pages/admin/Dashboard';
import StreetAnalysis from './pages/admin/StreetAnalysis';
import History from './pages/admin/History';
import Incidents from './pages/Incidents';
import Requests from './pages/Requests';
import RequestDetail from './pages/RequestDetail';
import Notifications from './pages/Notifications';
import Search from './pages/Search';
import { Profile, Settings } from './pages/Account';
import OfficerDashboard from './pages/officer/Dashboard';
import UrbanOpsMap, { MapPoint } from './components/UrbanOpsMap';

function RequireRole({ role }: { role: Role }) {
  const { user, ready, boot } = useAuth();
  useEffect(() => { boot(); }, [boot]);
  if (!ready) return <Stage><div className="text-sm text-slate-500">Loading…</div></Stage>;
  if (!user) return <Navigate to="/login" replace />;
  if (user.role !== role) return <Navigate to={user.role === 'admin' ? '/admin' : '/officer'} replace />;
  return (
    <Shell role={role}>
      <Outlet />
    </Shell>
  );
}

function OfficerMap() {
  return (
    <Stage>
      <h1 className="font-display text-2xl font-bold">Field Map</h1>
      <MapGate />
    </Stage>
  );
}

function MapGate() {
  const [points, setPoints] = useState<MapPoint[]>([]);
  useEffect(() => {
    (async () => {
      const [r, s] = await Promise.all([api.get('/api/v1/requests'), api.get('/api/v1/streets')]);
      const coord = new Map<number, any>(s.data.map((x: any) => [x.id, x]));
      setPoints(
        r.data.filter((q: any) => !['resolved', 'rejected'].includes(q.status) && coord.get(q.street_id))
          .map((q: any) => {
            const st = coord.get(q.street_id);
            return { id: q.id, lat: st.latitude, lon: st.longitude, severity: q.severity, label: `${q.code} — ${st.name}`, kind: 'request' as const };
          }),
      );
    })().catch(console.error);
  }, []);
  return <UrbanOpsMap points={points} />;
}

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/login" element={<Login />} />
        <Route path="/faq" element={<Faq />} />
        <Route element={<RequireRole role="admin" />}>
          <Route path="/admin" element={<AdminDashboard />} />
          <Route path="/admin/streets" element={<StreetAnalysis />} />
          <Route path="/admin/history" element={<History />} />
          <Route path="/admin/incidents" element={<Incidents base="/admin" />} />
          <Route path="/admin/requests" element={<Requests base="/admin" />} />
          <Route path="/admin/requests/:id" element={<RequestDetail />} />
          <Route path="/admin/notifications" element={<Notifications />} />
          <Route path="/admin/search" element={<Search base="/admin" />} />
          <Route path="/admin/faq" element={<Faq />} />
          <Route path="/admin/settings" element={<Settings />} />
          <Route path="/admin/profile" element={<Profile />} />
        </Route>
        <Route element={<RequireRole role="officer" />}>
          <Route path="/officer" element={<OfficerDashboard />} />
          <Route path="/officer/queue" element={<Requests base="/officer" mineToggle />} />
          <Route path="/officer/map" element={<OfficerMap />} />
          <Route path="/officer/requests/:id" element={<RequestDetail />} />
          <Route path="/officer/notifications" element={<Notifications />} />
          <Route path="/officer/search" element={<Search base="/officer" />} />
          <Route path="/officer/faq" element={<Faq />} />
          <Route path="/officer/settings" element={<Settings />} />
          <Route path="/officer/profile" element={<Profile />} />
        </Route>
        <Route path="*" element={<Navigate to="/login" replace />} />
      </Routes>
    </BrowserRouter>
  );
}
