from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from datetime import date
    from entities.task_status import TaskStatus


@dataclass
class Task:
    task_id: int
    title: str
    description: str
    due_date: 'date'
    status: 'TaskStatus'
