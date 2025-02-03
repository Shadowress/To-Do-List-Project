from typing import TYPE_CHECKING

from datetime import datetime
from entities.task_status import TaskStatus

if TYPE_CHECKING:
    from entities import Task
    from filehandler import FileHandler


class TaskManager:
    def __init__(self, file_handler: 'FileHandler') -> None:
        self.file_handler = file_handler
        self._task_storage: dict[int, 'Task'] = {}

    def setup(self) -> None:
        self.file_handler.setup_file(self)

    def add_task_to_storage(self, task: 'Task') -> None:
        self._task_storage.update({task.task_id: task})

    @property
    def task_storage(self) -> tuple['Task', ...]:
        return tuple(list(self._task_storage.values()))

    def add_new_task(self, data: list[str]) -> None:
        task_id = int(data[0])
        title = data[1]
        description = data[2]
        due_date = datetime.strptime(data[3], "%Y-%m-%d")
        status = TaskStatus(data[4])

        task: 'Task' = Task(task_id, title, description, due_date, status)
        self.add_task_to_storage(task)
        self.file_handler.append_file(self, task)

    def delete_task(self) -> None:
        ...

    def edit_task(self) -> None:
        ...

    def find_tasks_by_title(self) -> list['Task']:
        ...
