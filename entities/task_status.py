from enum import Enum


class TaskStatus(Enum):
    PENDING: int = "Pending"
    IN_PROGRESS: int = "In Progress"
    COMPLETED: int = "Completed"
    OVERDUE: int = "Overdue"
