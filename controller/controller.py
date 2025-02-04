import threading
from typing import TYPE_CHECKING

import config
from common.exceptions import UnsupportedFileFormatError, FileDataError
from common.factory import create_file_handler, create_ui

if TYPE_CHECKING:
    from filehandler import FileHandler
    from services import TaskManager
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
        except (UnsupportedFileFormatError, FileDataError, PermissionError) as e:
            self.ui.display_error_and_exit(e)

    def add_task(self, task_data: list[str]) -> None:
        try:
            self.task_manager.operate_add_task(task_data)
            self.ui.display_message(f"Task added successfully.")
        # todo change
        except Exception as e:
            self.ui.display_error(f"Error adding task: {str(e)}")

    # todo change param
    def delete_task(self) -> None:
        try:
            self.task_manager.operate_delete_task()
            self.ui.display_message(f"Task deleted successfully.")
        # todo change
        except Exception as e:
            self.ui.display_error(f"Error deleting task: {str(e)}")

    def edit_task(self) -> None:
        ...

    def find_tasks_by_title(self) -> list['Task']:
        ...
