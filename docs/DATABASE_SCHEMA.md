# UrbanEyes database schema (Postgres 16 authoritative; SQLite-compatible dev fallback)

Mirrored by `backend/app/models/*.py`. `infra/postgres_init.sql` carries the CHECK constraints.
Migrations: `0001_initial` (full schema), `0002_detection_evidence` (dims + mask columns).

## Tables
- **organizations**(id, name UNIQUE, type, created_at)
- **users**(id, email UNIQUE INDEX, password_hash, full_name, role CHECK(admin|officer) INDEX,
  org_id FK→organizations NULL ON DELETE SET NULL, is_active, created_at, updated_at)
- **streets**(id, name INDEX, area INDEX, latitude, longitude, created_at)
- **videos**(id, street_id FK CASCADE INDEX, storage_key, filename, size_bytes, duration_s,
  status CHECK(ready|invalid), recorded_at, created_at)
- **analyses**(id, street_id FK CASCADE INDEX, video_id FK NULL SET NULL, created_by FK NULL SET NULL,
  status CHECK(queued|running|done|failed) INDEX, overall_severity CHECK(weak|medium|critical) NULL INDEX,
  weak/medium/critical_count, cat_road/waste/drainage/infra CHECK severity NULL,
  reason, recommendation, request_recommended, reasoning_source CHECK('local'), error, created_at)
- **detections**(id, analysis_id FK CASCADE INDEX, frame_index, label INDEX, category INDEX,
  severity CHECK INDEX, confidence, x1,y1,x2,y2, frame_width, frame_height, mask_area,
  mask_polygon) — internal/audit only. Frame dims are real extracted px (NULL = unknown);
  mask_area is a frame fraction; mask_polygon is compact JSON ≤32 pts (migration `0002`).
- **incidents**(id, analysis_id FK CASCADE UNIQUE, street_id FK CASCADE INDEX,
  severity CHECK INDEX, status CHECK(open|requested|resolved) INDEX, created_at)
- **municipal_requests**(id, code UNIQUE INDEX `UE-YYYY-NNNN`, incident_id FK CASCADE,
  analysis_id FK CASCADE, street_id FK CASCADE INDEX, submitted_by FK NULL SET NULL,
  assigned_to FK NULL SET NULL, status CHECK(pending|under_review|accepted|assigned|in_progress|resolved|rejected) INDEX,
  severity CHECK INDEX, note, created_at, updated_at)
- **request_status_history**(id, request_id FK CASCADE INDEX, actor_id FK NULL SET NULL,
  from_status NULL, to_status, reason, created_at) — every transition, append-only in practice
- **officer_assignments**(id, request_id FK CASCADE INDEX, officer_id FK CASCADE INDEX,
  assigned_by FK NULL SET NULL, created_at)
- **resolution_evidence**(id, request_id FK CASCADE INDEX, officer_id FK NULL SET NULL,
  kind CHECK(before|after|repair), storage_key, notes, created_at)
- **notifications**(id, user_id FK CASCADE INDEX, title, body, kind, is_read INDEX, created_at)
- **audit_logs**(id, actor_id NULL, action INDEX, entity INDEX, entity_id, meta_json, created_at) — append-only
- **refresh_tokens**(id, user_id FK CASCADE INDEX, jti UNIQUE INDEX, revoked, expires_at, created_at)

## Indexes & integrity
- B-tree on all FKs + composite `(street_id, created_at)` on analyses, `(user_id, created_at)`
  on notifications, `(request_id, created_at)` on history, `(street_id, status)` and
  `(assigned_to, status)` on requests, `(user_id, expires_at)` on refresh tokens.
- Severity/status CHECKs enforce the 3-level and 7-state invariants at the DB level, not just the API.
- Timestamps: `created_at` everywhere, `updated_at` on users + municipal_requests.
