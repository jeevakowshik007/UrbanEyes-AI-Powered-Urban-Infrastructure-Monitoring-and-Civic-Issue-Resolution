# UrbanEyes API specification — `GET /openapi.json` is authoritative; this is the human contract.

Base: `/api/v1`. Auth: `Authorization: Bearer <access>` except register/login/refresh.
Errors: `{detail, code}`. Severity literals everywhere: `weak | medium | critical`.
List endpoints accept `limit` (default 50) + `offset`, clamped to `PAGE_MAX_LIMIT` (200).

## Auth
| Method | Path | Role | Body → Response |
|---|---|---|---|
| POST | `/auth/register` | public | `{email,password,full_name,role}` → 201 `{access_token,refresh_token}` |
| POST | `/auth/login` | public | `{email,password}` → `{access_token,refresh_token}` |
| POST | `/auth/refresh` | public | `{refresh_token}` → rotated pair (old revoked) |
| POST | `/auth/logout` | user | `{refresh_token}` → 204 |
| POST | `/auth/logout-all` | user | revokes all own refresh tokens → 204 |
| GET | `/auth/me` | user | → `{id,email,full_name,role,org_id}` |

## Streets & videos
| GET `/streets` | admin,officer | → streets enriched with `video_count, latest_severity, latest_analysis_at` |
| GET `/streets/{id}` | admin,officer | → one enriched street |
| GET `/videos?street_id=` | admin,officer | → video list |
| POST `/videos/upload?street_id=` | admin | multipart `file` → 201 video or 422 `Video validation failed` |

## Analyses & incidents
| POST `/analyses` | admin | `{street_id, video_id?}` → 202 `{analysis_id, status: queued}`. 422 when no video. |
| GET `/analyses?street_id=` | admin,officer | user-facing severity counts + categories + reason + recommendation |
| GET `/analyses/{id}` | admin,officer | poll `queued/running/done/failed` |
| GET `/incidents?severity=` | admin,officer | open issues from completed analyses |

## Requests (explicit confirm — never auto-created)
| POST `/requests` | admin | `{analysis_id, note?}` → 201 `{code: UE-YYYY-NNNN, status: pending}`. 409 if duplicate |
| GET `/requests?status=&mine=` | admin (own), officer (all; `mine` filters assigned) |
| GET `/requests/{id}` | scoped | detail |
| PATCH `/requests/{id}/status` | officer | `{to_status, reason?}` — state machine guarded; 409 illegal, 422 rejected-without-reason / resolved-without-evidence |
| POST `/requests/{id}/assignments` | officer | `{officer_id}` → assigned (+ auto-transition) |
| POST `/requests/{id}/evidence?kind=before\|after\|repair` | officer | multipart image (≤25 MB) → 201 |
| POST `/requests/{id}/evidence?kind=before\|after\|repair` | officer | multipart image, magic-byte verified (JPEG/PNG/GIF/WebP, ≤`EVIDENCE_MAX_MB`) → 201 |
| GET `/requests/{id}/evidence` | scoped | resolution evidence list (same visibility as the request) |
| GET `/requests/{id}/history` | scoped | full auditable transition trail |
| GET `/files?key=` | scoped | local files stream (videos: any authed user; evidence: request visibility); S3 returns short-lived presigned-URL JSON |

## Ops
| GET `/notifications?unread_only=` (+`limit`/`offset`) | user | own notifications, newest first |
| PATCH `/notifications/{id}/read` | user | mark read |
| GET `/search?q=` | admin,officer | streets + request codes |
| GET `/dashboard` | admin,officer | real aggregates: critical counts, requests by status, recent analyses |
| GET `/health` (unauthenticated) | public | `{status, cv_provider, reasoning_provider, yolo: {installed, version, weights_present, device, cuda_available}}` |
