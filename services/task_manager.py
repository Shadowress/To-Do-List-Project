from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from entities import Task
    from filehandler import FileHandler


class TaskManager:
    def __init__(self, file_handler: 'FileHandler') -> None:
        self.file_handler = file_handler
        self._task_storage: list['Task'] = []

    def setup(self) -> None:
        self.file_handler.setup_file(self)
        print(self._task_storage)

    def add_task_to_storage(self, task: 'Task') -> None:
        self._task_storage.append(task)

    def add_new_task(self) -> None:
        ...

    def delete_task(self) -> None:
        ...

    def edit_task(self) -> None:
        ...

    def find_tasks_by_title(self) -> list['Task']:
        ...
