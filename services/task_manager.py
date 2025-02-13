from datetime import datetime
from typing import TYPE_CHECKING, Union, ValuesView

from common.exceptions import InvalidTaskDataError, TaskNotFoundError
from entities.task_status import TaskStatus

if TYPE_CHECKING:
    from entities import Task
    from filehandler import FileHandler


class TaskManager:
    def __init__(self, file_handler: 'FileHandler') -> None:
        self._file_handler: 'FileHandler' = file_handler
        self.DATE_FORMAT: str = "%Y-%m-%d"
        self._task_storage: dict[int, 'Task'] = {}

    def setup(self) -> None:
        self._file_handler.setup(self)
        self._check_overdue_tasks()

    def add_task_to_storage(self, task: 'Task') -> None:
        self._task_storage.update({task.task_id: task})

    def operate_add_task(self, data: dict[str, Union[str, 'datetime']]) -> None:
        try:
            task_id = self._get_next_task_id()
            title = data["title"]
            description = data["description"]
            due_date = data["due_date"]
            status = TaskStatus.PENDING

            task: 'Task' = Task(task_id, title, description, due_date, status)

            self.add_task_to_storage(task)
            self._file_handler.append_file(self.DATE_FORMAT, task)  # todo might change to run on thread

        except (IndexError, ValueError, TypeError) as e:
            raise InvalidTaskDataError(f"Invalid task data provided: {str(e)}")

    def _get_next_task_id(self) -> int:
        task_storage: dict[int, 'Task'] = self._task_storage

        if not task_storage:
            return 1

        return max(task_storage.keys()) + 1

    def operate_delete_task(self, task_id: int) -> None:
        try:
            del self._task_storage[task_id]
            # todo might change to run on thread
            self._file_handler.write_file(list(self._task_storage.values()), self.DATE_FORMAT)

        except KeyError as e:
            raise TaskNotFoundError(f"Task with id {task_id} not found: {str(e)}")

    def operate_edit_task(self, task_id: int, data: dict[str, Union[str, 'datetime']]) -> None:
        try:
            task: 'Task' = self._task_storage[task_id]

            if data["title"]:
                task.title = data["title"]

            if data["description"]:
                task.description = data["description"]

            if data["due_date"]:
                task.due_date = data["due_date"]

                if TaskStatus.OVERDUE.value == task.status and datetime.now() < data["due_date"]:
                    task.status = TaskStatus.PENDING

            if data["status"]:
                task.status = TaskStatus(data["status"])

            # todo might change to run on thread
            self._file_handler.write_file(list(self._task_storage.values()), self.DATE_FORMAT)

        except (IndexError, ValueError, TypeError) as e:
            raise InvalidTaskDataError(f"Invalid task data provided: {str(e)}")

        except KeyError as e:
            raise TaskNotFoundError(f"Task with id {task_id} not found: {str(e)}")

    def get_tasks_by_title(self, title_filter: str) -> tuple['Task', ...]:
        return tuple(task for task in self.task_storage if title_filter.lower() in task.title.lower())

    def get_tasks_by_status(self, status_filter: str) -> tuple['Task', ...]:
        return tuple(task for task in self.task_storage if task.status == status_filter)

    def _check_overdue_tasks(self) -> None:
        tasks: ValuesView['Task'] = self._task_storage.values()
        is_changed: bool = False

        for task in tasks:
            if "Completed" != task.status and datetime.now() > task.due_date:
                task.status = TaskStatus.OVERDUE
                is_changed = True

        if is_changed:
            # todo might change to run on thread
            self._file_handler.write_file(list(self._task_storage.values()), self.DATE_FORMAT)

    @property
    def task_storage(self) -> tuple['Task', ...]:
        self._check_overdue_tasks()
        return tuple(list(self._task_storage.values()))
