from datetime import datetime
from typing import TYPE_CHECKING

from common.exceptions import InvalidTaskDataError, TaskNotFoundError
from entities.task_status import TaskStatus

if TYPE_CHECKING:
    from entities import Task
    from filehandler import FileHandler


class TaskManager:
    def __init__(self, file_handler: 'FileHandler') -> None:
        self.file_handler: 'FileHandler' = file_handler
        self.date_format: str = "%Y-%m-%d"
        self._task_storage: dict[int, 'Task'] = {}

    def setup(self) -> None:
        self.file_handler.setup(self)

    def add_task_to_storage(self, task: 'Task') -> None:
        self._task_storage.update({task.task_id: task})

    @property
    def task_storage(self) -> tuple['Task', ...]:
        return tuple(list(self._task_storage.values()))

    def operate_add_task(self, data: list[str]) -> None:
        try:
            task_id = self._get_next_task_id()
            title = data[0]
            description = data[1]
            due_date = datetime.strptime(data[2], self.date_format)
            status = TaskStatus(data[3])

            task: 'Task' = Task(task_id, title, description, due_date, status)

            self.add_task_to_storage(task)
            self.file_handler.append_file(self, task)
        except (IndexError, ValueError, TypeError) as e:
            raise InvalidTaskDataError(f"Invalid task data provided: {str(e)}")

    def _get_next_task_id(self) -> int:
        task_storage: dict[int, 'Task'] = self._task_storage

        if not task_storage:
            return 1

        else:
            return max(task_storage.keys()) + 1

    def operate_delete_task(self, task_id: int) -> None:
        try:
            del self._task_storage[task_id]
            self.file_handler.write_file(self)
        except KeyError as e:
            raise TaskNotFoundError(f"Task with id {task_id} not found: {str(e)}")

    def operate_edit_task(self) -> None:
        ...

    def find_tasks_by_title(self) -> list['Task']:
        ...
