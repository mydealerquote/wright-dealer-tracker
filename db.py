import os
import sqlite3
from contextlib import contextmanager

DB_PATH = os.environ.get("DB_PATH", "data.sqlite")

@contextmanager
def get_conn():
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    try:
        yield conn
    finally:
        conn.commit()
        conn.close()

def init_db():
    with get_conn() as conn:
        cur = conn.cursor()
        cur.execute("""
        CREATE TABLE IF NOT EXISTS runs (
            run_id INTEGER PRIMARY KEY AUTOINCREMENT,
            started_at TEXT NOT NULL,
            finished_at TEXT,
            status TEXT NOT NULL,
            total_points INTEGER NOT NULL,
            points_done INTEGER NOT NULL DEFAULT 0,
            dealers_seen INTEGER NOT NULL DEFAULT 0,
            error TEXT
        );
        """)
        cur.execute("""
        CREATE TABLE IF NOT EXISTS dealers (
            dealer_id INTEGER PRIMARY KEY AUTOINCREMENT,
            dealer_key TEXT NOT NULL UNIQUE,
            name TEXT,
            address1 TEXT,
            city TEXT,
            state TEXT,
            zip TEXT,
            phone TEXT,
            website TEXT,
            lat REAL,
            lng REAL,
            first_seen_run_id INTEGER,
            last_seen_run_id INTEGER
        );
        """)
