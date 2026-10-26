# UrbanEyes — AI-Assisted Urban Infrastructure Analysis & Municipal Response Platform

Observe → Analyze → Understand → Prioritize → Request → Act → Verify → Resolve

No external LLM. No API keys for reasoning. The pipeline is
**Video → YOLO26-Seg → evidence aggregation → deterministic severity →
Local Urban Infrastructure Reasoning Engine → Admin review → municipal request →
Officer workflow → resolution evidence → Resolved.**

## What is production-capable vs mock/development

| Component | Status | Notes |
|---|---|---|
| FastAPI backend, JWT+RBAC, request lifecycle, audit | Production-capable | Tested (attack + e2e + integrity suites) |
| Local Reasoning Engine | Production-capable | Deterministic, offline, factor-scored, tested |
| Postgres schema + Alembic `0001_initial` | Production-capable | Compose runs migrations automatically |
| Celery + Redis task boundary | Production-capable | Needs Redis; dev runs in-process |
| S3/MinIO storage abstraction | Production-capable | Needs S3/MinIO; dev uses local disk |
| YOLO26-Seg inference | **Production-capable** | Fine-tuned on 1,243 pothole images (mAP50≈0.55). `CV_PROVIDER=yolo` active |
| Google Maps | Production-capable | Live Google Maps JS API with street pins. `VITE_GOOGLE_MAPS_KEY` required; falls back to free MapLibre |

The UI always shows the true vision mode (`Development vision (mock detections)` vs `YOLO26-Seg vision`).

## Monorepo layout

```
urbaneyes/
  backend/          # FastAPI + SQLAlchemy + Alembic + CV/reasoning + Celery tasks
    app/
      main.py                 # app factory (prod skips DDL; migrations own prod)
      core/                   # config, security, deps (RBAC + safe sessions), rate_limit, logging
      db/                     # base, session (Postgres pooling / SQLite dev)
      models/                 # 14 SQLAlchemy tables
      schemas/                # Pydantic contracts (Weak/Medium/Critical only)
      api/v1/                 # auth, streets, videos, analyses, requests, files, ops
      services/               # video_pipeline, ai (YOLO), reasoning (local), requests, storage, seed
      workers/                # celery_app + task boundary (no duplicated pipeline logic)
    alembic/                  # env.py + versions/0001_initial.py
    tests/ requirements.txt Dockerfile .env.example pyproject.toml (ruff)
  frontend/         # React + TS + Vite + Tailwind + MapLibre + Recharts
  infra/            # docker-compose.yml (db, redis, minio+mc, api, worker, web), postgres_init.sql
  docs/             # ARCHITECTURE.md, API_SPEC.md, DATABASE_SCHEMA.md
```

## Local setup (dev: SQLite + local disk + in-process tasks)

```powershell
# Backend :8000
cd backend
python -m venv .venv; .\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
copy .env.example .env
uvicorn app.main:app --reload --port 8000

# Frontend :5173 (new terminal)
cd frontend
npm install
npm run dev
```

Open http://localhost:5173 (use `localhost`, not `127.0.0.1`, to match default CORS).
Demo logins (when `SEED_DEMO=true`): `admin@urbaneyes.city / Admin123!`, `officer@urbaneyes.city / Officer123!`.

## Docker setup (production-like: Postgres + Redis + MinIO + worker)

```powershell
$env:DB_PASSWORD="strong-db-password"
$env:MINIO_USER="urbaneyes"
$env:MINIO_PASSWORD="strong-minio-password-min-32-chars!!"
docker compose -f infra/docker-compose.yml up --build
```

App at http://localhost:8080, API at :8000, MinIO console at :9001.
The `api` service runs `alembic upgrade head` before serving; `mc` bootstraps the bucket.

## Required environment variables (backend)

`DATABASE_URL`, `JWT_SECRET` (32+ random chars, required in prod), `CORS_ORIGINS`,
`CV_PROVIDER` (mock|yolo), `REASONING_PROVIDER` (local), `STORAGE_PROVIDER` (local|s3),
`S3_ENDPOINT/BUCKET/ACCESS_KEY/SECRET_KEY` (when s3), `REDIS_URL` (enables Celery worker),
`YOLO26_SEG_WEIGHTS`, `YOLO26_CONF`. Full list with defaults: `backend/.env.example`.

## Real YOLO weight setup

A fine-tuned YOLO26-Seg model is already trained and bundled at `backend/weights/yolo26-street-damage.pt`.

**Training pipeline** (reproducible via `backend/tools/`):

1. **Dataset**: 1,243 pothole images from [jaygala24/pothole-detection](https://github.com/jaygala24/pothole-detection) (YOLO box format, single class `pothole`).
2. **Prepare**: `python tools/prepare_pothole_dataset.py` — converts boxes to 4-corner polygons for segmentation training, splits 85/15 train/val.
3. **Train**: `python tools/train_yolo26.py 35` — fine-tunes `yolo26n-seg.pt` (pretrained COCO) on CPU, imgsz=416, batch=16, ~2.5h on 16-core CPU.
4. **Result**: mAP50 ≈ 0.55 after 8 epochs (best.pt auto-saved each epoch).

**Configuration** (already set in `backend/.env`):

```
CV_PROVIDER=yolo
YOLO26_SEG_WEIGHTS=./weights/yolo26-street-damage.pt
YOLO26_IMGSZ=416
YOLO26_CONF=0.35
```

The UI badge shows `YOLO26-Seg vision` when active. To revert to mock: set `CV_PROVIDER=mock`.

## Google Maps setup

1. Get a Google Maps JS API key from Google Cloud Console (billing required).
2. Add HTTP referrers: `http://localhost:5173/*` and `http://127.0.0.1:5173/*`.
3. Set `VITE_GOOGLE_MAPS_KEY` in `frontend/.env`.
4. Restart frontend. The map loads with street pins; click a pin to pick a street.

Without a key (or if referrers don't match), the app falls back to free MapLibre tiles automatically.

## Demo video

`demo/street_drive_demo.mp4` — synthetic street-drive clip (18s, 1280×720) with real pothole-photo patches composited onto the road. Generated by `backend/tools/make_demo_video.py`. Upload it to any street to test the full pipeline.

## PostgreSQL setup

- Compose: automatic (data in `pgdata` volume, constraints from `postgres_init.sql`).
- External Postgres: point `DATABASE_URL` at it and run `cd backend; alembic upgrade head`.
- Dev stays on SQLite unless `DATABASE_URL` is overridden — no code changes needed.

## Test commands

```powershell
cd backend
python -m pytest tests -q          # backend: 57 tests (auth/RBAC/attack/lifecycle/reasoning/e2e/integrity/migration/yolo)
python -m ruff check app tests alembic
cd ../frontend
npm run build                      # tsc + vite production build
npx playwright test                # UI E2E vs live :5173 + :8000 (desktop + mobile, sequential workers)
```
