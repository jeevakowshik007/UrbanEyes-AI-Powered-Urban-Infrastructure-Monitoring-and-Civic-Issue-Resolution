import { create } from 'zustand';
import api from '../services/api';

export type Role = 'admin' | 'officer';
export interface User {
  id: number;
  email: string;
  full_name: string;
  role: Role;
}

interface AuthState {
  user: User | null;
  ready: boolean;
  login: (email: string, password: string) => Promise<Role>;
  register: (email: string, password: string, full_name: string, role: Role) => Promise<Role>;
  logout: () => Promise<void>;
  boot: () => Promise<void>;
}

export const useAuth = create<AuthState>((set) => ({
  user: null,
  ready: false,
  login: async (email, password) => {
    const { data } = await api.post('/api/v1/auth/login', { email, password });
    localStorage.setItem('ue_access', data.access_token);
    localStorage.setItem('ue_refresh', data.refresh_token);
    const me = (await api.get('/api/v1/auth/me')).data as User;
    set({ user: me });
    return me.role;
  },
  register: async (email, password, full_name, role) => {
    const { data } = await api.post('/api/v1/auth/register', { email, password, full_name, role });
    localStorage.setItem('ue_access', data.access_token);
    localStorage.setItem('ue_refresh', data.refresh_token);
    const me = (await api.get('/api/v1/auth/me')).data as User;
    set({ user: me });
    return me.role;
  },
  logout: async () => {
    try {
      await api.post('/api/v1/auth/logout', { refresh_token: localStorage.getItem('ue_refresh') });
    } catch { /* best effort */ }
    localStorage.removeItem('ue_access');
    localStorage.removeItem('ue_refresh');
    set({ user: null });
  },
  boot: async () => {
    if (!localStorage.getItem('ue_access')) return set({ ready: true });
    try {
      const me = (await api.get('/api/v1/auth/me')).data as User;
      set({ user: me, ready: true });
    } catch {
      set({ user: null, ready: true });
    }
  },
}));
