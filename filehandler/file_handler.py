import os.path
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from services import TaskManager


class FileHandler(ABC):

    def __init__(self, file_path: str):
        self.file_path = file_path

    def setup_file(self, data_storage: 'TaskManager') -> None:
        if not os.path.exists(self.file_path):
            self.create_file()
            return

        # todo add check permission exception
        if open(self.file_path, 'r'):
            ...

        if self.is_file_empty():
            return

        self.load_file(data_storage)

    def create_file(self) -> None:
        open(self.file_path, 'x').close()

    def is_file_empty(self) -> bool:
        return os.path.getsize(self.file_path) == 0

    @abstractmethod
    def load_file(self, data_storage: 'TaskManager') -> None:
        ...

    @abstractmethod
    def write_file(self) -> None:
        ...

    @abstractmethod
    def append_file(self) -> None:
        ...
