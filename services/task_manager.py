from datetime import datetime
from typing import TYPE_CHECKING

from entities.task_status import TaskStatus

if TYPE_CHECKING:
    from entities import Task
    from filehandler import FileHandler


class TaskManager:
    def __init__(self, file_handler: 'FileHandler') -> None:
        self.file_handler = file_handler
        self.date_format = "%Y-%m-%d"
        self._task_storage: dict[int, 'Task'] = {}

    def setup(self) -> None:
        self.file_handler.setup(self)

    def add_task_to_storage(self, task: 'Task') -> None:
        self._task_storage.update({task.task_id: task})

    @property
    def task_storage(self) -> tuple['Task', ...]:
        return tuple(list(self._task_storage.values()))

    def operate_add_task(self, data: list[str]) -> None:
        # todo change the task_id to be auto increment
        task_id = int(data[0])
        title = data[1]
        description = data[2]
        due_date = datetime.strptime(data[3], self.date_format)
        status = TaskStatus(data[4])

        task: 'Task' = Task(task_id, title, description, due_date, status)
        self.add_task_to_storage(task)
        self.file_handler.append_file(self, task)

    def operate_delete_task(self) -> None:
        ...

    def operate_edit_task(self) -> None:
        ...

    def find_tasks_by_title(self) -> list['Task']:
        ...
