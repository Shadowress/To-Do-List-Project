import os.path
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from services import TaskManager
    from entities import Task


def _create_file(file_path: str) -> None:
    open(file_path, "x").close()


def _check_file_permission(file_path: str) -> bool:
    try:
        open(file_path, "r+").close()
        return True

    except PermissionError:
        return False


def _is_file_empty(file_path: str) -> bool:
    return os.path.getsize(file_path) == 0


class FileHandler(ABC):
    def __init__(self, file_path: str):
        self.file_path: str = file_path

    def setup(self, data_storage: 'TaskManager') -> None:
        file_path: str = self.file_path

        if not os.path.exists(file_path):
            _create_file(file_path)
            return

        if not _check_file_permission(file_path):
            raise PermissionError(f"Permission denied: Unable to access or modify the file '{file_path}'")

        if _is_file_empty(file_path):
            return

        self.load_file(data_storage)

    @abstractmethod
    def load_file(self, data_storage: 'TaskManager') -> None:
        ...

    @abstractmethod
    def write_file(self, data_storage: 'TaskManager') -> None:
        ...

    @abstractmethod
    def append_file(self, data_storage: 'TaskManager', task: 'Task') -> None:
        ...
