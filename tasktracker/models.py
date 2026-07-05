from dataclasses import dataclass, asdict
from datetime import datetime, timezone

PRIORITIES = ("low", "medium", "high")


@dataclass
class Task:
    id: int
    title: str
    done: bool = False
    created_at: str = ""
    priority: str = "medium"

    def __post_init__(self):
        if not self.created_at:
            self.created_at = datetime.now(timezone.utc).isoformat()
        if self.priority not in PRIORITIES:
            raise ValueError(f"priority must be one of {PRIORITIES}, got {self.priority!r}")

    def to_dict(self):
        return asdict(self)

    @classmethod
    def from_dict(cls, data):
        return cls(**data)
