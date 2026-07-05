import pytest
from pathlib import Path

from tasktracker.models import Task
from tasktracker.storage import load_tasks, save_tasks, next_id


def test_save_and_load_round_trip(tmp_path: Path):
    path = tmp_path / "tasks.json"
    tasks = [Task(id=1, title="write tests")]

    save_tasks(tasks, path=path)
    loaded = load_tasks(path=path)

    assert len(loaded) == 1
    assert loaded[0].id == 1
    assert loaded[0].title == "write tests"
    assert loaded[0].done is False
    assert loaded[0].priority == "medium"


def test_priority_round_trips(tmp_path: Path):
    path = tmp_path / "tasks.json"
    tasks = [Task(id=1, title="fix prod bug", priority="high")]

    save_tasks(tasks, path=path)
    loaded = load_tasks(path=path)

    assert loaded[0].priority == "high"


def test_invalid_priority_raises():
    with pytest.raises(ValueError):
        Task(id=1, title="bad", priority="urgent")


def test_load_missing_file_returns_empty_list(tmp_path: Path):
    path = tmp_path / "missing.json"
    assert load_tasks(path=path) == []


def test_next_id_increments_from_max():
    tasks = [Task(id=1, title="a"), Task(id=5, title="b")]
    assert next_id(tasks) == 6


def test_next_id_starts_at_one_when_empty():
    assert next_id([]) == 1
