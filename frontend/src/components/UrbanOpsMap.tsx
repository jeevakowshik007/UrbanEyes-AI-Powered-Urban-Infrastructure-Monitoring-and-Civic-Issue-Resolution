import { useEffect, useRef, useState } from 'react';
import maplibregl from 'maplibre-gl';
import { SEV_COLOR } from './ui';

export interface MapPoint {
  id: number;
  lat: number;
  lon: number;
  severity?: string | null;
  label: string;
  kind?: 'street' | 'request';
}

const GOOGLE_KEY = (import.meta.env.VITE_GOOGLE_MAPS_KEY as string | undefined)?.trim();
const HOME: [number, number] = [77.5946, 12.9716];
const NEAREST_PICK_KM = 1.5;

declare global {
  interface Window {
    google?: any;
    __ue_gmaps?: Promise<void>;
    gm_authFailure?: () => void;
  }
}

function loadGoogleMaps(key: string): Promise<void> {
  if (window.google?.maps) return Promise.resolve();
  if (!window.__ue_gmaps) {
    window.__ue_gmaps = new Promise((resolve, reject) => {
      const s = document.createElement('script');
      s.src = `https://maps.googleapis.com/maps/api/js?key=${encodeURIComponent(key)}&v=weekly`;
      s.async = true;
      s.onload = () => resolve();
      s.onerror = () => reject(new Error('Google Maps script failed to load'));
      document.head.appendChild(s);
    });
  }
  return window.__ue_gmaps;
}

function pickColor(p: MapPoint): string {
  return SEV_COLOR[p.severity ?? ''] ?? (p.kind === 'request' ? '#4567A8' : '#7FBF9B');
}

function haversineKm(aLat: number, aLon: number, bLat: number, bLon: number): number {
  const R = 6371;
  const dLat = ((bLat - aLat) * Math.PI) / 180;
  const dLon = ((bLon - aLon) * Math.PI) / 180;
  const s =
    Math.sin(dLat / 2) ** 2 +
    Math.cos((aLat * Math.PI) / 180) * Math.cos((bLat * Math.PI) / 180) * Math.sin(dLon / 2) ** 2;
  return 2 * R * Math.asin(Math.sqrt(s));
}

export default function UrbanOpsMap({
  points,
  onSelect,
  height = 420,
}: {
  points: MapPoint[];
  onSelect?: (p: MapPoint) => void;
  height?: number;
}) {
  const ref = useRef<HTMLDivElement>(null);
  const mapRef = useRef<any>(null);
  const markersRef = useRef<any[]>([]);
  const providerRef = useRef<'google' | 'maplibre' | null>(null);
  const selectRef = useRef(onSelect);
  selectRef.current = onSelect;
  const pointsRef = useRef(points);
  pointsRef.current = points;
  const [failed, setFailed] = useState(false);

  const clearMarkers = () => {
    for (const m of markersRef.current) {
      try {
        if (m?.setMap) m.setMap(null); // google marker
        else m?.remove?.(); // maplibre marker
      } catch {
        /* map already gone */
      }
    }
    markersRef.current = [];
  };

  const selectNearest = (lng: number, lat: number) => {
    let best: MapPoint | null = null;
    let bestKm = Infinity;
    for (const p of pointsRef.current) {
      if (!p.lat || !p.lon) continue;
      const d = haversineKm(lat, lng, p.lat, p.lon);
      if (d < bestKm) {
        bestKm = d;
        best = p;
      }
    }
    if (best && bestKm <= NEAREST_PICK_KM) selectRef.current?.(best);
  };

  const renderPoints = () => {
    const provider = providerRef.current;
    const map = mapRef.current;
    if (!provider || !map) return;
    clearMarkers();
    const pts = pointsRef.current.filter((p) => p.lat && p.lon);

    if (provider === 'maplibre') {
      const bounds = new maplibregl.LngLatBounds();
      for (const p of pts) {
        const el = document.createElement('div');
        el.className = 'map-marker';
        el.title = p.label;
        el.style.background = pickColor(p);
        el.onclick = () => selectRef.current?.(p);
        markersRef.current.push(new maplibregl.Marker({ element: el }).setLngLat([p.lon, p.lat]).addTo(map));
        bounds.extend([p.lon, p.lat]);
      }
      if (pts.length > 1 && !bounds.isEmpty()) {
        try { map.fitBounds(bounds, { padding: 60, maxZoom: 14 }); } catch { /* not ready */ }
      } else if (pts.length === 1) {
        map.flyTo({ center: [pts[0].lon, pts[0].lat], zoom: 14 });
      }
      return;
    }

    const g = window.google.maps;
    const bounds = new g.LatLngBounds();
    for (const p of pts) {
      const m = new g.Marker({
        position: { lat: p.lat, lng: p.lon },
        map,
        title: p.label,
        icon: {
          path: g.SymbolPath.CIRCLE,
          scale: 9,
          fillColor: pickColor(p),
          fillOpacity: 1,
          strokeColor: '#ffffff',
          strokeWeight: 2,
        },
      });
      m.addListener('click', () => selectRef.current?.(p));
      markersRef.current.push(m);
      bounds.extend({ lat: p.lat, lng: p.lon });
    }
    if (pts.length > 1) map.fitBounds(bounds, { padding: 60 });
    else if (pts.length === 1) { map.setCenter({ lat: pts[0].lat, lng: pts[0].lon }); map.setZoom(14); }
  };

  useEffect(() => {
    if (!ref.current || mapRef.current) return;
    const container = ref.current;
    let cancelled = false;

    const initMapLibre = () => {
      if (cancelled || mapRef.current) return;
      try {
        const canvas = document.createElement('canvas');
        if (!(canvas.getContext('webgl2') || canvas.getContext('webgl'))) {
          setFailed(true);
          return;
        }
        const map = new maplibregl.Map({
          container,
          style: import.meta.env.VITE_MAP_STYLE_URL as string,
          center: HOME,
          zoom: 11,
        });
        map.addControl(new maplibregl.NavigationControl(), 'top-right');
        map.addControl(new maplibregl.GeolocateControl({ positionOptions: { enableHighAccuracy: true } }), 'top-right');
        map.on('click', (e) => selectNearest(e.lngLat.lng, e.lngLat.lat));
        mapRef.current = map;
        providerRef.current = 'maplibre';
        renderPoints();
      } catch {
        setFailed(true);
      }
    };

    const initGoogle = async () => {
      if (!GOOGLE_KEY) { initMapLibre(); return; }
      try {
        await loadGoogleMaps(GOOGLE_KEY);
      } catch {
        if (!cancelled) initMapLibre();
        return;
      }
      if (cancelled) return;
      window.gm_authFailure = () => {
        if (cancelled) return;
        clearMarkers();
        try { mapRef.current?.setMap?.(null); } catch { /* ignore */ }
        mapRef.current = null;
        providerRef.current = null;
        container.innerHTML = '';
        initMapLibre();
      };
      try {
        const map = new window.google.maps.Map(container, {
          center: { lat: HOME[1], lng: HOME[0] },
          zoom: 11,
          mapTypeControl: false,
          fullscreenControl: false,
          streetViewControl: false,
          backgroundColor: '#e8edf2',
        });
        window.google.maps.event.addListener(map, 'click', (e: any) =>
          selectNearest(e.latLng.lng(), e.latLng.lat()),
        );
        mapRef.current = map;
        providerRef.current = 'google';
        renderPoints();
      } catch {
        initMapLibre();
      }
    };

    initGoogle();
    return () => {
      cancelled = true;
      clearMarkers();
      try { mapRef.current?.remove?.(); } catch { /* already gone */ }
      mapRef.current = null;
      providerRef.current = null;
    };
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  useEffect(() => {
    renderPoints();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [points]);

  return (
    <div className="rounded-2xl overflow-hidden shadow-float border border-white/60" style={{ height }}>
      {failed ? (
        <div className="w-full h-full grid place-items-center bg-white/60 px-6 text-center">
          <p className="text-sm text-slate-500">
            Interactive map unavailable on this device. All streets and requests remain
            fully usable in the lists on this page.
          </p>
        </div>
      ) : (
        <div ref={ref} style={{ width: '100%', height: '100%' }} />
      )}
    </div>
  );
}
