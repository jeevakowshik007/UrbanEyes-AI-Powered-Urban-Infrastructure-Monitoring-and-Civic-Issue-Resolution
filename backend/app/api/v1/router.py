"""v1 router aggregation (flat list — included directly by the app factory)."""
from app.api.v1 import analyses, auth, files, misc, requests, streets

v1_routers = [auth.router, streets.router, analyses.router, requests.router, files.router, misc.router]
