from dataclasses import dataclass
from datetime import datetime

from entities.task_status import TaskStatus


@dataclass
class Task:
    _task_id: int
    _title: str
    _description: str
    _due_date: 'datetime'
    _status: 'TaskStatus'

    def __init__(self, task_id: int, title: str, description: str, due_date: 'datetime', status: 'TaskStatus') -> None:
        self.task_id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    @property
    def task_id(self) -> int:
        return self._task_id

    @property
    def title(self) -> str:
        return self._title

    @property
    def description(self) -> str:
        return self._description

    @property
    def due_date(self) -> 'datetime':
        return self._due_date

    @property
    def status(self) -> str:
        return self._status.value

    @task_id.setter
    def task_id(self, value: int) -> None:
        self._task_id = value

    @title.setter
    def title(self, value: str) -> None:
        if not value:
            raise ValueError("Title cannot be empty")

        self._title = value

    @description.setter
    def description(self, value: str) -> None:
        if not value:
            raise ValueError("Description cannot be empty")

        self._description = value

    @due_date.setter
    def due_date(self, value: 'datetime') -> None:
        if not isinstance(value, datetime):
            raise TypeError("Due date must be a datetime object")

        self._due_date = value.replace(hour=0, minute=0, second=0, microsecond=0)

    @status.setter
    def status(self, value: 'TaskStatus') -> None:
        if not isinstance(value, TaskStatus):
            raise ValueError(f"Invalid status: {value}")

        self._status = value
