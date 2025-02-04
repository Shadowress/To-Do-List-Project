from typing import TYPE_CHECKING

from .file_handler import FileHandler

if TYPE_CHECKING:
    from entities import Task
    from services import TaskManager


class JSONFileHandler(FileHandler):
    def load_file(self, data_storage: 'TaskManager') -> None:
        pass

    def write_file(self, data_storage: 'TaskManager') -> None:
        pass

    def append_file(self, data_storage: 'TaskManager', task: 'Task') -> None:
        pass
