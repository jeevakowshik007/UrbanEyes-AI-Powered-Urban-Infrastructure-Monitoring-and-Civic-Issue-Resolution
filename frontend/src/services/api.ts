import axios from 'axios';

const api = axios.create({ baseURL: import.meta.env.VITE_API_URL || 'http://localhost:8000' });

let refreshing: Promise<string> | null = null;

async function doRefresh(): Promise<string> {
  const rt = localStorage.getItem('ue_refresh');
  if (!rt) throw new Error('no refresh token');
  const { data } = await axios.post(
    `${import.meta.env.VITE_API_URL || 'http://localhost:8000'}/api/v1/auth/refresh`,
    { refresh_token: rt },
  );
  localStorage.setItem('ue_access', data.access_token);
  localStorage.setItem('ue_refresh', data.refresh_token);
  return data.access_token;
}

api.interceptors.request.use((cfg) => {
  const t = localStorage.getItem('ue_access');
  if (t) cfg.headers.Authorization = `Bearer ${t}`;
  return cfg;
});

api.interceptors.response.use(
  (r) => r,
  async (err) => {
    const orig = err.config;
    if (err.response?.status === 401 && orig && !orig._retried) {
      orig._retried = true;
      try {
        refreshing ||= doRefresh();
        const t = await refreshing;
        refreshing = null;
        orig.headers.Authorization = `Bearer ${t}`;
        return api(orig);
      } catch {
        refreshing = null;
        localStorage.removeItem('ue_access');
        localStorage.removeItem('ue_refresh');
        window.location.href = '/login';
      }
    }
    return Promise.reject(err);
  },
);

export default api;
