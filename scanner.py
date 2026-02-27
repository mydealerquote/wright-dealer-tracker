from datetime import datetime, timezone
from typing import Dict, List, Tuple
import time

from db import get_conn
from fetcher import fetch_dealers_near

def utc_now_iso():
    return datetime.now(timezone.utc).isoformat()

def dealer_key(d: Dict):
    return "|".join([
        (d.get("name") or "").strip().lower(),
        (d.get("address1") or "").strip().lower(),
        (d.get("city") or "").strip().lower(),
        (d.get("state") or "").strip().lower(),
        (d.get("zip") or "").strip().lower(),
    ])

def generate_lower48_grid(step_deg: float = 0.25):
    lat_min, lat_max = 24.5, 49.5
    lng_min, lng_max = -124.8, -66.9
    points = []
    lat = lat_min
    while lat <= lat_max:
        lng = lng_min
        while lng <= lng_max:
            points.append((round(lat, 6), round(lng, 6)))
            lng += step_deg
        lat += step_deg
    return points

def create_run(step_deg: float):
    points = generate_lower48_grid(step_deg)
    with get_conn() as conn:
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO runs (started_at, status, total_points)
            VALUES (?, 'running', ?)
        """, (utc_now_iso(), len(points)))
        return cur.lastrowid
