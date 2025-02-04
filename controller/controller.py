import threading
from typing import TYPE_CHECKING

import config
from common.exceptions import FileDataError, InvalidTaskDataError, TaskNotFoundError, \
    FileWriteError
from common.factory import create_file_handler, create_ui
from services import TaskManager

if TYPE_CHECKING:
    from filehandler import FileHandler
    from ui import UI
    from entities import Task


class Controller:
    def __init__(self) -> None:
        self.ui: 'UI' = create_ui(config.UI)
        file_handler: 'FileHandler' = create_file_handler(config.FILE_PATH, self.ui)
        self.task_manager: 'TaskManager' = TaskManager(file_handler)

    def start(self) -> None:
        try:
            threading.Thread(self.task_manager.setup())
            self.ui.run_main_menu(self)
        except (FileDataError, PermissionError) as e:
            self.ui.display_error_and_exit(e)
        except Exception as e:
            self.ui.display_error_and_exit(e)

    def add_task(self, task_data: list[str]) -> None:
        try:
            self.task_manager.operate_add_task(task_data)
            self.ui.display_message(f"Task added successfully.")
        except (InvalidTaskDataError, FileWriteError) as e:
            self.ui.display_error(e)

    def delete_task(self, task_id: int) -> None:
        try:
            self.task_manager.operate_delete_task(task_id)
            self.ui.display_message(f"Task deleted successfully.")
        except (TaskNotFoundError, FileWriteError) as e:
            self.ui.display_error(e)

    def edit_task(self) -> None:
        ...

    def find_tasks_by_title(self) -> list['Task']:
        ...
