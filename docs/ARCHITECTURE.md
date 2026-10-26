# UrbanEyes — Complete Production Architecture

> Observe → Analyze → Understand → Prioritize → Request → Act → Verify → Resolve

## 1. Complete architecture (summary)

Modular full-stack monorepo. Three runtime boundaries: `frontend` (SPA), `backend` (FastAPI),
`workers` (in-process BackgroundTasks now, Celery/Redis later). Postgres is the system of record.
S3-compatible storage holds videos/frames/evidence. YOLO26-Seg sits behind an
isolated vision-provider interface (`CV_PROVIDER=mock|yolo`); reasoning is the
built-in Local Urban Infrastructure Reasoning Engine (`REASONING_PROVIDER=local`)
— deterministic, offline, no API key or network needed.

```
                    ┌──────────────── FRONTEND (React+TS) ────────────────┐
                    │ Admin shell          │ Officer shell                │
                    │ Dashboard/Map/Street │ Queue/Map/Request detail     │
                    │ History/Incidents/   │ Evidence upload              │
                    │ Requests/Notify/FAQ  │ Notifications                │
                    └────────────┬─────────┴──────────────┬───────────────┘
                                 │ HTTPS/JSON (JWT)       │
                    ┌────────────▼────────────────────────▼───────────────┐
                    │ BACKEND (FastAPI, modular routers)                 │
                    │ auth │ streets │ videos │ analyses │ incidents │    │
                    │ requests │ assignments │ evidence │ notify │ search  │
                    │ RBAC deps │ audit middleware │ rate limit │ CORS     │
                    ├────────────────────────────────────────────────────┤
                    │ SERVICES (business logic, no HTTP in here)         │
                    │ video_pipeline → yolo_adapter → severity_service → │
                    │ local_reasoning (validated) → analysis_pipeline →   │
                    │ request_service (state machine) → notification_svc │
                    └──┬──────────────┬──────────────┬───────────────────┘
                       │              │              │
              ┌────────▼──────┐ ┌─────▼──────┐ ┌────▼──────────┐
              │ Postgres 16   │ │ S3-compat  │ │ CV providers  │
              │ (SQLAlchemy + │ │ (boto3 /   │ │ YOLO26-Seg    │
              │  Alembic)     │ │  local fs) │ │ (mock | yolo) │
              └───────────────┘ └────────────┘ └───────────────┘
```

ASCII system diagram (data flow for one street analysis):

```
Admin selects street → GET /streets/{id} → GET /videos?street_id=
  → POST /analyses (street_id, video_id) → 202 Accepted {analysis_id, status: queued}
  → worker: validate → extract frames → YOLO26-Seg → aggregate → severity rules
  → local reasoning engine (factor scoring) → validate → persist analysis+incident
  → websocket/poll → admin sees severity UI
  → if critical: modal "Review evidence → Submit Municipal Request"
  → POST /requests → officer queue → lifecycle transitions (each audited)
  → officer uploads after-images → RESOLVED → admin verifies
```

## 2–9. Sub-architectures

### Frontend (`frontend/src/`)
- `pages/admin/`: Dashboard, StreetAnalysis, History, Incidents, Requests, Notifications, FAQ, Search, Settings, Profile.
- `pages/officer/`: OfficerDashboard, Queue, RequestDetail, MapView, Notifications.
- `components/UrbanOpsMap.tsx`: MapLibre wrapper (markers, filters, popups, fly-to).
- `components/ui.tsx`: GlassCard, SeverityBadge (weak/medium/critical only), ConfirmRequestModal, EvidenceGallery, TrendChart.
- `components/ProviderBadge.tsx`: honest vision/reasoning mode indicator from `/health`.
- `services/api.ts`: axios instance + JWT refresh; `services/download.ts`: auth file downloads; `store/`: zustand `useAuth`.
- Route guards: `<RequireRole role="admin|officer">`. No raw detection counts rendered in primary UI.

### Backend (`backend/app/`)
- `main.py`: app factory, CORS, headers, rate limit, router mount `/api/v1`, global error handler (no leak).
- `core/`: `config.py` (pydantic-settings), `security.py` (bcrypt + JWT), `deps.py` (get_current_user, require_role, audited transitions), `rate_limit.py`, `logging.py`.
- `api/v1/`: one router file per domain; thin handlers → service calls.
- `services/`: pure business logic, each with a single responsibility (see §AI).
- `workers/`: Celery app (`celery_app.py`) + task boundary (`tasks.py`). ONE pipeline
  implementation in `services/pipeline.py`; tasks only route (Celery worker when `REDIS_URL`
  is set, eager in-process dev mode otherwise) — no duplicated logic.

### Database
Postgres 16. SQLAlchemy 2.0 + Alembic (`backend/alembic/`, initial `0001_initial` migration
matching the models). Full DDL in `docs/DATABASE_SCHEMA.md` and `infra/postgres_init.sql`.
Tables: users, organizations, streets, videos, analyses, detections (raw, internal), severity_assessments,
incidents, municipal_requests, request_status_history, officer_assignments, resolution_evidence,
notifications, audit_logs. Indexes on FKs, composite `(street_id, created_at)` on analyses,
`(user_id, created_at)` on notifications, `(request_id, created_at)` on history,
`(street_id, status)` on requests, GIN/trgm-ready text fields for search.

### AI/CV
- `SegmentationProvider` interface → `YOLO26SegAdapter` (tested `ultralytics==8.4.142`,
  which ships the genuine `yolo26-seg.yaml`; checkpoint NOT bundled) and
  `DevHeuristicAdapter` (only when `CV_PROVIDER=mock`; deterministic from file hash —
  clearly labeled dev-only, emits VGA frame dims so reasoning stays realistic).
- Startup/runtime validation for `CV_PROVIDER=yolo`: ultralytics import → checkpoint path →
  file existence → model load → class names, each with an actionable error. Mock mode
  never touches Ultralytics.
- Pipeline: validate video → sample `FRAME_SAMPLE_COUNT` evenly spaced frames deterministically
  (count-based; the old `FRAME_SAMPLE_FPS` setting was removed) → per-frame `predict`
  with wired `YOLO26_CONF/DEVICE/IMGSZ/IOU/MAX_DET` (+ optional CUDA-only fp16) →
  boxes always, `masks.xy` polygons (≤32 pts) + mask area when the model is a real seg
  checkpoint, bbox fallback otherwise → actual frame dims from `orig_shape` on every detection.
- Class mapping is normalization-tolerant (case/space/underscore) against the app vocabulary;
  checkpoint labels outside it become auditable `unmapped` findings excluded from scoring.
- Per-finding `CLASS_SEVERITY_PRIOR` is informational only; FINAL severity always comes from
  the LocalReasoningEngine's evidence factors (confidence, persistence, real normalized area,
  repetition, impact).
- Raw boxes/dims/masks persist to `detections` (internal/audit only, migration `0002`;
  polygons capped, never raw tensors), never in primary UI payloads.

### Local Urban Infrastructure Reasoning Engine (`services/reasoning.py`)
- Purely local and deterministic: factor scoring over CV evidence only — frequency (30%),
  frame persistence (25%), mean confidence (20%), affected area (15%), repetition (10%) —
  scaled by per-category operational impact, then thresholded (`REASONING_SCORE_CRITICAL=0.60`,
  `REASONING_SCORE_MEDIUM=0.32`, all configurable via env).
- Reasons only from provided evidence (category, confidence, bbox area, frames, repetition,
  co-occurrence). Malformed entries are repaired or counted invalid; low-confidence findings
  are filtered; empty evidence yields Weak with routine-monitoring guidance. Never crashes.
- Output validated by the `ReasoningOutput` pydantic model (overall_severity, weak/medium/critical
  counts, 4 categories, reason, recommendation, municipal_request_recommended). Stored output holds
  concise factor summaries only — no chain-of-thought. `reasoning_source` is always `"local"`.
- Request policy: Critical → recommended=true; Weak → false; Medium → true when
  medium+critical findings reach `MEDIUM_REQUEST_MIN_FINDINGS` (default 3). Critical NEVER
  auto-creates a request; admin confirmation is still mandatory.

### Auth
JWT access (15 min) + rotating refresh (7 d). bcrypt (passlib). RBAC: `admin`, `officer` roles, `require_role`
dependency on every router. Refresh endpoint rotates + revokes (jti allowlist table or stateless + short TTL —
  implemented as DB-backed refresh tokens for revocation). Password rules enforced server-side.

### Request lifecycle (state machine, `request_service.py`)
```
PENDING → UNDER_REVIEW → ACCEPTED → ASSIGNED → IN_PROGRESS → RESOLVED
              ↓              ↓           ↓            ↓
           REJECTED       REJECTED    (reassign)  (reopen→IN_PROGRESS)
```
- All transitions validated against allowed map; illegal → 409. Every transition writes
  `request_status_history` (actor, from→to, reason, timestamp) + `audit_logs` + notification to the other role.
- Critical analyses NEVER auto-create requests; UI forces explicit confirm modal → `POST /requests`.

## 10. Folder structure
See `README.md` tree. Monorepo: `backend/`, `frontend/`, `infra/`, `docs/`, `storage/` (local-dev only, gitignored content).

## 11. API specification
Full contract in `docs/API_SPEC.md` (~35 endpoints). Highlights:
- `POST /api/v1/auth/{register,login,refresh,logout,me}`
- `GET/POST /api/v1/streets`, `GET /api/v1/streets/{id}`
- `POST /api/v1/videos/upload` (multipart, validated), `GET /api/v1/videos?street_id=`
- `POST /api/v1/analyses` → 202 `{analysis_id}`; `GET /api/v1/analyses/{id}`; `GET /api/v1/analyses?street_id=`
- `GET /api/v1/incidents`, `GET /api/v1/incidents/{id}`
- `POST /api/v1/requests` (admin, requires confirmed analysis), `GET /api/v1/requests`,
  `GET /api/v1/requests/{id}`, `PATCH /api/v1/requests/{id}/status` (officer, state-machine guarded),
  `POST /api/v1/requests/{id}/assignments`, `POST /api/v1/requests/{id}/evidence` (multipart)
- `GET /api/v1/notifications`, `PATCH /api/v1/notifications/{id}/read`, `GET /api/v1/search?q=`
- Errors: `{detail, code}` envelope; 401/403/404/409/422 used correctly.

## 12. Database schema
See `docs/DATABASE_SCHEMA.md` + `infra/postgres_init.sql` (authoritative DDL) mirrored by SQLAlchemy models.
Key constraints: severity CHECKs limited to 3 values; request status CHECK to 7 values; FK cascades;
`created_at/updated_at` everywhere; `audit_logs` append-only.

## 13. Development phases
1. ✅ Architecture + scaffold (this doc). 2. Backend domain + auth + AI adapters + lifecycle (now).
3. Seed data + tests. 4. Frontend shells + map + workflows. 5. Storage + notifications + search polish.
6. Hardening (rate limits, audit, e2e) + deploy docs.

## 14. Dependencies
Backend: fastapi, uvicorn, sqlalchemy, alembic, psycopg, pydantic, pydantic-settings,
python-jose[cryptography], passlib[bcrypt], python-multipart, boto3, httpx, slowapi, opencv-python-headless,
ultralytics (optional, only for real YOLO), pytest/httpx. Frontend: react, react-router, zustand, axios,
maplibre-gl, recharts, framer-motion, tailwindcss.

## 15. Environment variables
See `.env.example` (root + backend + frontend). Secrets only server-side; `VITE_*` holds only public URLs.

## 16. Local development setup
```powershell
# backend (SQLite dev, local storage, in-process tasks — no keys needed)
cd backend; python -m venv .venv; .\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
copy .env.example .env
uvicorn app.main:app --reload --port 8000
# frontend
cd frontend; npm install; copy .env.example .env; npm run dev  # :5173
```
Migrations (prod/compose run these automatically): `cd backend; alembic upgrade head`.
Full production-like demo (Postgres + Redis + MinIO + worker): see `infra/docker-compose.yml` —
`docker compose -f infra/docker-compose.yml up --build` (set `DB_PASSWORD`/`MINIO_*` in env).

## 17. Deployment architecture
Docker Compose: `api` (FastAPI, runs `alembic upgrade head` then uvicorn), `db` (postgres:16),
`redis` (task broker), `worker` (celery, same image), `minio` + one-shot `mc` bucket bootstrap
(S3-compat storage), `web` (nginx serving built SPA). Healthchecks on db/redis/minio/api;
`api`/`web` start only when dependencies are healthy. Managed Postgres + object
storage + secret manager in production; 2+ API replicas behind LB; migrations run as init job.

## 18. Testing strategy
pytest: auth/RBAC matrix (incl. refresh reuse detection + logout-all), state-machine
illegal-transition tests, local-reasoning factor/threshold/policy tests,
`ReasoningOutput` schema tests, upload-validation (incl. image magic bytes) tests,
pagination tests, storage-backend unit tests, Alembic migration test on a throwaway DB. Frontend: vitest for severity utils +
guards; Playwright e2e (admin analyze→confirm→request, officer accept→resolve) in CI later.

## 19. Security strategy
bcrypt, short JWT + rotating refresh, RBAC on every route, CORS allowlist, slowapi limits on
auth/upload/analyses, file magic+size validation, no stack traces to client, audit_logs on mutations,
`JWT_SECRET` env-only (no external AI keys exist — reasoning is local), least-privilege DB role.

## 20. Risks and mitigation
| Risk | Mitigation |
|---|---|
| YOLO26 weights unavailable | Provider interface + mock adapter; real weights via `YOLO26_SEG_WEIGHTS` path, CI skips without them |
| Local reasoning mis-scores novel evidence | Factor weights/thresholds env-configurable, factor summaries auditable per analysis, human confirm still required for critical |
| Large video uploads | Size caps, background processing, 202+polling, frame sampling caps |
| Map tile dependency | Configurable `VITE_MAP_STYLE_URL`, Carto free default, offline-degraded list views |
| Postgres unavailable locally | SQLite dev fallback via `DATABASE_URL`; Postgres in compose/prod |
| Scope creep on severities | CHECK constraints + Literals enforce exactly 3 levels everywhere |
