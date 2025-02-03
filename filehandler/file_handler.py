import os.path
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from services import TaskManager
    from entities import Task


def create_file(file_path: str) -> None:
    open(file_path, "x").close()


def check_file_permission(file_path: str) -> bool:
    try:
        with open(file_path, "r+"):
            pass
        return True
    except PermissionError:
        return False


def is_file_empty(file_path: str) -> bool:
    return os.path.getsize(file_path) == 0


class FileHandler(ABC):

    def __init__(self, file_path: str):
        self.file_path = file_path

    def setup_file(self, data_storage: 'TaskManager') -> None:
        file_path: str = self.file_path

        if not os.path.exists(file_path):
            create_file(file_path)
            return

        if not check_file_permission(file_path):
            raise PermissionError(f"Permission denied: Unable to access or modify the file '{file_path}'")

        if is_file_empty(file_path):
            return

        self.load_file(data_storage)

    @abstractmethod
    def load_file(self, data_storage: 'TaskManager') -> None:
        ...

    @abstractmethod
    def write_file(self, data_storage: 'TaskManager') -> None:
        ...

    @abstractmethod
    def append_file(self, data_storage: 'TaskManager', new_data: 'Task') -> None:
        ...
