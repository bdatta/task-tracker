# task-tracker

A simple command-line task tracker.

## Usage

```
python -m tasktracker.cli add "buy milk"
python -m tasktracker.cli list
python -m tasktracker.cli list --all
python -m tasktracker.cli done 1
python -m tasktracker.cli rm 1
```

Tasks are stored in `tasks.json` in the current directory.
