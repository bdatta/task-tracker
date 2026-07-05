from tasktracker.models import Task
from tasktracker.storage import load_tasks, save_tasks, next_id


def add(title: str, priority: str = "medium") -> Task:
    tasks = load_tasks()
    task = Task(id=next_id(tasks), title=title, priority=priority)
    tasks.append(task)
    save_tasks(tasks)
    return task


def list_tasks(show_all: bool = True) -> list[Task]:
    tasks = load_tasks()
    if show_all:
        return tasks
    return [task for task in tasks if not task.done]


def mark_done(task_id: int) -> Task | None:
    tasks = load_tasks()
    for task in tasks:
        if task.id == task_id:
            task.done = True
            save_tasks(tasks)
            return task
    return None


def remove(task_id: int) -> bool:
    tasks = load_tasks()
    remaining = [task for task in tasks if task.id != task_id]
    if len(remaining) == len(tasks):
        return False
    save_tasks(remaining)
    return True
