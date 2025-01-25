import datetime
from dataclasses import dataclass

from entities.task_status import TaskStatus


@dataclass
class Task:
    title: str
    description: str
    due_date: datetime
    status: TaskStatus
