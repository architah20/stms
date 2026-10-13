"""STMS - Student Task Management System (Flask + SQLite)."""
import os
import sqlite3

from flask import Flask, jsonify, redirect, render_template, request
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)  # exposes /metrics for Prometheus/Grafana
metrics.info("stms_app_info", "STMS application info", version="1.0.0")

DB_PATH = os.environ.get("DB_PATH", "tasks.db")


def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    with get_db() as db:
        db.execute(
            """CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                due_date TEXT,
                priority TEXT DEFAULT 'Medium',
                done INTEGER DEFAULT 0
            )"""
        )


@app.route("/")
def index():
    with get_db() as db:
        tasks = db.execute("SELECT * FROM tasks ORDER BY done, due_date").fetchall()
    total = len(tasks)
    completed = sum(1 for t in tasks if t["done"])
    return render_template("index.html", tasks=tasks, total=total, completed=completed)



@app.route("/add", methods=["POST"])
def add():
    title = request.form.get("title", "").strip()
    due_date = request.form.get("due_date") or None
    priority = request.form.get("priority", "Medium").strip()

    allowed_priorities = {"Low", "Medium", "High"}

    if title and len(title) <= 200:
        if priority not in allowed_priorities:
            priority = "Medium"

        with get_db() as db:
            db.execute(
                """INSERT INTO tasks (title, due_date, priority)
                   VALUES (?, ?, ?)""",
                (title, due_date, priority),
            )

    return redirect("/")



@app.route("/edit/<int:task_id>", methods=["POST"])
def edit(task_id):
    title = request.form.get("title", "").strip()
    if title:
        with get_db() as db:
            db.execute("UPDATE tasks SET title=? WHERE id=?", (title, task_id))
    return redirect("/")


@app.route("/complete/<int:task_id>")
def complete(task_id):
    with get_db() as db:
        db.execute("UPDATE tasks SET done=1 WHERE id=?", (task_id,))
    return redirect("/")


@app.route("/delete/<int:task_id>")
def delete(task_id):
    with get_db() as db:
        db.execute("DELETE FROM tasks WHERE id=?", (task_id,))
    return redirect("/")


@app.route("/api/tasks")
def api_tasks():
    with get_db() as db:
        rows = db.execute("SELECT * FROM tasks").fetchall()
    return jsonify([dict(r) for r in rows])


@app.route("/health")
def health():
    return jsonify(status="ok")


init_db()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
