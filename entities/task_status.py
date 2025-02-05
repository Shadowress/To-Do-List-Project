from enum import Enum


class TaskStatus(Enum):
    PENDING: str = "Pending"
    IN_PROGRESS: str = "In Progress"
    COMPLETED: str = "Completed"
    OVERDUE: str = "Overdue"
