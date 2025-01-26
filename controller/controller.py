import threading
from typing import TYPE_CHECKING

import filehandler
from services import TaskManager

if TYPE_CHECKING:
    from ui import UI


class Controller:
    def __init__(self, file_path: str, ui: 'UI'):
        self.file_path = f"data/{file_path}"
        self.ui = ui

    def start(self) -> None:
        try:
            file_handler = filehandler.init(self.file_path)
            task_manager = TaskManager(file_handler)
            threading.Thread(task_manager.setup())
            self.ui.run_main_menu(self)
        # todo change accepting Exception as general
        except Exception as e:
            self.ui.display_error_and_exit(e)
