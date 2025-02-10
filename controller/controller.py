import threading
from typing import TYPE_CHECKING

from common.exceptions import FileDataError, InvalidTaskDataError, TaskNotFoundError, FileWriteError
from common.factory import create_file_handler, create_ui
from services import TaskManager

if TYPE_CHECKING:
    from filehandler import FileHandler
    from ui import UI
    from entities import Task


class Controller:
    def __init__(self) -> None:
        self._ui: 'UI' = create_ui(self)
        file_handler: 'FileHandler' = create_file_handler(self._ui)
        self._task_manager: 'TaskManager' = TaskManager(file_handler)

    def start(self) -> None:
        try:
            threading.Thread(target=self._task_manager.setup()).start()
            self._ui.run()

        except (FileDataError, PermissionError) as e:
            self._ui.display_error_and_exit(e)

        # todo uncomment ltr
        # except Exception as e:
        #     self._ui.display_error_and_exit(e)

    def get_all_tasks(self) -> tuple['Task', ...]:
        return self._task_manager.task_storage

    def add_task(self, task_data: list[str]) -> None:
        try:
            self._task_manager.operate_add_task(task_data)
            self._ui.display_message(f"Task added successfully")

        except (InvalidTaskDataError, FileWriteError) as e:
            self._ui.display_error(e)

    def delete_task(self, task_id: int) -> None:
        try:
            self._task_manager.operate_delete_task(task_id)
            self._ui.display_message(f"Task deleted successfully")

        except (TaskNotFoundError, FileWriteError) as e:
            self._ui.display_error(e)

    def edit_task(self, task_id: int, task_data: list[str]) -> None:
        try:
            self._task_manager.operate_edit_task(task_id, task_data)
            self._ui.display_message(f"Task updated successfully")

        except (InvalidTaskDataError, TaskNotFoundError, FileWriteError) as e:
            self._ui.display_error(e)

    def get_tasks_by_title(self, title_filter: str) -> tuple['Task', ...]:
        return self._task_manager.get_tasks_by_title(title_filter)
