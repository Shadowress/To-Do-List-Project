from enum import Enum, auto


class TaskStatus(Enum):
    PENDING: int = auto()
    IN_PROGRESS: int = auto()
    COMPLETED: int = auto()
    OVERDUE: int = auto()
    CANCELLED: int = auto()
