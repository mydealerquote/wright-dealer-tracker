import csv
import io
from db import get_conn

def export_current_csv():
    with get_conn() as conn:
        rows = conn.execute("SELECT name, address1, city, state, zip, phone, website FROM dealers").fetchall()
    out = io.StringIO()
    w = csv.writer(out)
    w.writerow(["name","address1","city","state","zip","phone","website"])
    for r in rows:
        w.writerow([r[c] for c in r.keys()])
    return out.getvalue()
