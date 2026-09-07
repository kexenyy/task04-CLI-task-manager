from task04 import add_task, mark_done, filter_tasks


def test_add_task():
    tasks = []
    add_task(tasks, "Study Python", "2026-09-10")

    assert tasks[0]["title"] == "Study Python"
    assert tasks[0]["status"] == "pending"


def test_mark_done():
    tasks = [
        {
            "title": "Study Python",
            "due": "2026-09-10",
            "status": "pending"
        }
    ]

    mark_done(tasks, 1)

    assert tasks[0]["status"] == "done"


def test_filter_by_status():
    tasks = [
        {
            "title": "Task 1",
            "due": "2026-09-10",
            "status": "done"
        },
        {
            "title": "Task 2",
            "due": "2026-09-11",
            "status": "pending"
        }
    ]

    result = filter_tasks(tasks, status="done")

    assert len(result) == 1
    assert result[0]["title"] == "Task 1"