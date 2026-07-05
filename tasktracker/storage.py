import json
from pathlib import Path

from tasktracker.models import Task

DEFAULT_PATH = Path("tasks.json")


def load_tasks(path: Path = DEFAULT_PATH) -> list[Task]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)
    return [Task.from_dict(item) for item in data]


def save_tasks(tasks: list[Task], path: Path = DEFAULT_PATH) -> None:
    with path.open("w", encoding="utf-8") as f:
        json.dump([task.to_dict() for task in tasks], f, indent=2)


def next_id(tasks: list[Task]) -> int:
    return max((task.id for task in tasks), default=0) + 1
