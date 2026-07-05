import argparse
import sys

from tasktracker import commands


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="tasktracker", description="A simple command-line task tracker")
    subparsers = parser.add_subparsers(dest="command", required=True)

    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("title", help="Task description")

    list_parser = subparsers.add_parser("list", help="List tasks")
    list_parser.add_argument("--all", action="store_true", help="Include completed tasks")

    done_parser = subparsers.add_parser("done", help="Mark a task as done")
    done_parser.add_argument("id", type=int, help="Task id")

    rm_parser = subparsers.add_parser("rm", help="Remove a task")
    rm_parser.add_argument("id", type=int, help="Task id")

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command == "add":
        task = commands.add(args.title)
        print(f"Added task {task.id}: {task.title}")

    elif args.command == "list":
        tasks = commands.list_tasks(show_all=args.all)
        if not tasks:
            print("No tasks found.")
        for task in tasks:
            status = "x" if task.done else " "
            print(f"[{status}] {task.id}: {task.title}")

    elif args.command == "done":
        task = commands.mark_done(args.id)
        if task is None:
            print(f"No task with id {args.id}", file=sys.stderr)
            return 1
        print(f"Marked task {task.id} as done")

    elif args.command == "rm":
        removed = commands.remove(args.id)
        if not removed:
            print(f"No task with id {args.id}", file=sys.stderr)
            return 1
        print(f"Removed task {args.id}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
