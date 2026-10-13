import os
import tempfile

os.environ["DB_PATH"] = os.path.join(tempfile.mkdtemp(), "test.db")

from app import app  # noqa: E402


def client():
    return app.test_client()


def test_health():
    r = client().get("/health")
    assert r.status_code == 200
    assert r.get_json()["status"] == "ok"


def test_home_page_loads():
    assert client().get("/").status_code == 200


def test_add_task():
    c = client()
    c.post("/add", data={"title": "Finish DevOps lab", "priority": "High"})
    tasks = c.get("/api/tasks").get_json()
    assert any(t["title"] == "Finish DevOps lab" for t in tasks)


def test_complete_and_delete_task():
    c = client()
    c.post("/add", data={"title": "Temp task"})
    task = [t for t in c.get("/api/tasks").get_json() if t["title"] == "Temp task"][0]
    c.get(f"/complete/{task['id']}")
    done = [t for t in c.get("/api/tasks").get_json() if t["id"] == task["id"]][0]
    assert done["done"] == 1
    c.get(f"/delete/{task['id']}")
    assert all(t["id"] != task["id"] for t in c.get("/api/tasks").get_json())


def test_metrics_endpoint():
    assert client().get("/metrics").status_code == 200

def test_invalid_priority_defaults_to_medium():
    c = client()
    c.post(
        "/add",
        data={"title": "Test priority validation", "priority": "Urgent"},
    )

    tasks = c.get("/api/tasks").get_json()
    task = [
        t for t in tasks
        if t["title"] == "Test priority validation"
    ][0]

    assert task["priority"] == "Medium"

