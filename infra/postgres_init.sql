-- UrbanEyes Postgres init: roles/levels enforced at the DB level.
CREATE TABLE IF NOT EXISTS organizations(
  id SERIAL PRIMARY KEY, name VARCHAR(160) UNIQUE NOT NULL,
  type VARCHAR(40) NOT NULL DEFAULT 'municipal', created_at TIMESTAMPTZ NOT NULL DEFAULT now());
CREATE TABLE IF NOT EXISTS users(
  id SERIAL PRIMARY KEY, email VARCHAR(255) UNIQUE NOT NULL, password_hash VARCHAR(255) NOT NULL,
  full_name VARCHAR(160) NOT NULL, role VARCHAR(20) NOT NULL CHECK (role IN ('admin','officer')),
  org_id INT REFERENCES organizations(id) ON DELETE SET NULL,
  is_active BOOLEAN NOT NULL DEFAULT TRUE,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(), updated_at TIMESTAMPTZ NOT NULL DEFAULT now());
CREATE INDEX IF NOT EXISTS ix_users_email ON users(email);
CREATE TABLE IF NOT EXISTS streets(
  id SERIAL PRIMARY KEY, name VARCHAR(200) NOT NULL, area VARCHAR(200) NOT NULL DEFAULT '',
  latitude DOUBLE PRECISION NOT NULL, longitude DOUBLE PRECISION NOT NULL,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now());
CREATE INDEX IF NOT EXISTS ix_streets_name ON streets(name);
CREATE TABLE IF NOT EXISTS videos(
  id SERIAL PRIMARY KEY, street_id INT NOT NULL REFERENCES streets(id) ON DELETE CASCADE,
  storage_key VARCHAR(512) NOT NULL, filename VARCHAR(255) NOT NULL, size_bytes INT NOT NULL,
  duration_s DOUBLE PRECISION, status VARCHAR(20) NOT NULL DEFAULT 'ready' CHECK (status IN ('ready','invalid')),
  recorded_at TIMESTAMPTZ, created_at TIMESTAMPTZ NOT NULL DEFAULT now());
CREATE TABLE IF NOT EXISTS analyses(
  id SERIAL PRIMARY KEY, street_id INT NOT NULL REFERENCES streets(id) ON DELETE CASCADE,
  video_id INT REFERENCES videos(id) ON DELETE SET NULL,
  created_by INT REFERENCES users(id) ON DELETE SET NULL,
  status VARCHAR(20) NOT NULL DEFAULT 'done' CHECK (status IN ('queued','running','done','failed')),
  overall_severity VARCHAR(20) CHECK (overall_severity IN ('weak','medium','critical')),
  weak_count INT NOT NULL DEFAULT 0, medium_count INT NOT NULL DEFAULT 0, critical_count INT NOT NULL DEFAULT 0,
  cat_road VARCHAR(20) CHECK (cat_road IN ('weak','medium','critical')),
  cat_waste VARCHAR(20) CHECK (cat_waste IN ('weak','medium','critical')),
  cat_drainage VARCHAR(20) CHECK (cat_drainage IN ('weak','medium','critical')),
  cat_infra VARCHAR(20) CHECK (cat_infra IN ('weak','medium','critical')),
  reason TEXT, recommendation TEXT, request_recommended BOOLEAN,
  reasoning_source VARCHAR(20) NOT NULL DEFAULT 'local' CHECK (reasoning_source = 'local'),
  error TEXT, created_at TIMESTAMPTZ NOT NULL DEFAULT now());
CREATE INDEX IF NOT EXISTS ix_analyses_street_time ON analyses(street_id, created_at);
CREATE TABLE IF NOT EXISTS detections(
  id SERIAL PRIMARY KEY, analysis_id INT NOT NULL REFERENCES analyses(id) ON DELETE CASCADE,
  frame_index INT NOT NULL, label VARCHAR(80) NOT NULL, category VARCHAR(40) NOT NULL,
  severity VARCHAR(20) NOT NULL CHECK (severity IN ('weak','medium','critical')),
  confidence DOUBLE PRECISION NOT NULL, x1 DOUBLE PRECISION NOT NULL, y1 DOUBLE PRECISION NOT NULL,
  x2 DOUBLE PRECISION NOT NULL, y2 DOUBLE PRECISION NOT NULL,
  frame_width DOUBLE PRECISION, frame_height DOUBLE PRECISION,
  mask_area DOUBLE PRECISION, mask_polygon TEXT);
CREATE INDEX IF NOT EXISTS ix_detections_analysis ON detections(analysis_id);
CREATE TABLE IF NOT EXISTS incidents(
  id SERIAL PRIMARY KEY, analysis_id INT NOT NULL UNIQUE REFERENCES analyses(id) ON DELETE CASCADE,
  street_id INT NOT NULL REFERENCES streets(id) ON DELETE CASCADE,
  severity VARCHAR(20) NOT NULL CHECK (severity IN ('weak','medium','critical')),
  status VARCHAR(20) NOT NULL DEFAULT 'open' CHECK (status IN ('open','requested','resolved')),
  created_at TIMESTAMPTZ NOT NULL DEFAULT now());
CREATE TABLE IF NOT EXISTS municipal_requests(
  id SERIAL PRIMARY KEY, code VARCHAR(24) UNIQUE NOT NULL,
  incident_id INT NOT NULL REFERENCES incidents(id) ON DELETE CASCADE,
  analysis_id INT NOT NULL REFERENCES analyses(id) ON DELETE CASCADE,
  street_id INT NOT NULL REFERENCES streets(id) ON DELETE CASCADE,
  submitted_by INT REFERENCES users(id) ON DELETE SET NULL,
  assigned_to INT REFERENCES users(id) ON DELETE SET NULL,
  status VARCHAR(20) NOT NULL DEFAULT 'pending'
    CHECK (status IN ('pending','under_review','accepted','assigned','in_progress','resolved','rejected')),
  severity VARCHAR(20) NOT NULL CHECK (severity IN ('weak','medium','critical')),
  note TEXT, created_at TIMESTAMPTZ NOT NULL DEFAULT now(), updated_at TIMESTAMPTZ NOT NULL DEFAULT now());
CREATE INDEX IF NOT EXISTS ix_requests_status ON municipal_requests(status);
CREATE TABLE IF NOT EXISTS request_status_history(
  id SERIAL PRIMARY KEY, request_id INT NOT NULL REFERENCES municipal_requests(id) ON DELETE CASCADE,
  actor_id INT REFERENCES users(id) ON DELETE SET NULL,
  from_status VARCHAR(20), to_status VARCHAR(20) NOT NULL, reason TEXT,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now());
CREATE INDEX IF NOT EXISTS ix_history_request ON request_status_history(request_id);
CREATE TABLE IF NOT EXISTS officer_assignments(
  id SERIAL PRIMARY KEY, request_id INT NOT NULL REFERENCES municipal_requests(id) ON DELETE CASCADE,
  officer_id INT NOT NULL REFERENCES users(id) ON DELETE CASCADE,
  assigned_by INT REFERENCES users(id) ON DELETE SET NULL,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now());
CREATE TABLE IF NOT EXISTS resolution_evidence(
  id SERIAL PRIMARY KEY, request_id INT NOT NULL REFERENCES municipal_requests(id) ON DELETE CASCADE,
  officer_id INT REFERENCES users(id) ON DELETE SET NULL,
  kind VARCHAR(20) NOT NULL CHECK (kind IN ('before','after','repair')),
  storage_key VARCHAR(512) NOT NULL, notes TEXT, created_at TIMESTAMPTZ NOT NULL DEFAULT now());
CREATE TABLE IF NOT EXISTS notifications(
  id SERIAL PRIMARY KEY, user_id INT NOT NULL REFERENCES users(id) ON DELETE CASCADE,
  title VARCHAR(200) NOT NULL, body TEXT NOT NULL DEFAULT '', kind VARCHAR(40) NOT NULL DEFAULT 'info',
  is_read BOOLEAN NOT NULL DEFAULT FALSE, created_at TIMESTAMPTZ NOT NULL DEFAULT now());
CREATE INDEX IF NOT EXISTS ix_notifications_user ON notifications(user_id);
CREATE TABLE IF NOT EXISTS audit_logs(
  id SERIAL PRIMARY KEY, actor_id INT REFERENCES users(id) ON DELETE SET NULL,
  action VARCHAR(80) NOT NULL, entity VARCHAR(80) NOT NULL, entity_id VARCHAR(80) NOT NULL,
  meta_json TEXT NOT NULL DEFAULT '{}', created_at TIMESTAMPTZ NOT NULL DEFAULT now());
CREATE TABLE IF NOT EXISTS refresh_tokens(
  id SERIAL PRIMARY KEY, user_id INT NOT NULL REFERENCES users(id) ON DELETE CASCADE,
  jti VARCHAR(64) UNIQUE NOT NULL, revoked BOOLEAN NOT NULL DEFAULT FALSE,
  expires_at TIMESTAMPTZ NOT NULL, created_at TIMESTAMPTZ NOT NULL DEFAULT now());
