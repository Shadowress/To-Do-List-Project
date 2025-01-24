import datetime
from entities.task_status import TaskStatus


class Task:

    def __init__(self, title: str, description: str, due_date: datetime, status: TaskStatus) -> None:
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def __str__(self) -> str:
        return (f"Book Title: {self.title}"
                f"Description: {self.description}"
                f"Due Date: {self.due_date}"
                f"Status: {self.status}")
