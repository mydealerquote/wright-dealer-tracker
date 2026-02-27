from flask import Flask, Response, render_template_string
from db import init_db
from export import export_current_csv

app = Flask(__name__)
init_db()

@app.route("/")
def index():
    return render_template_string("<h2>Wright Dealer Tracker Running</h2><a href='/export'>Download CSV</a>")

@app.route("/export")
def export():
    csv_text = export_current_csv()
    return Response(csv_text, mimetype="text/csv", headers={"Content-Disposition": "attachment; filename=dealers_current.csv"})
