import filehandler
from common.exceptions import UnsupportedFileFormat
from services import TaskManager
from ui import UI


class Controller:
    def __init__(self, file_path: str, ui: UI):
        self.file_path = file_path
        self.ui = ui

    def start(self) -> None:
        try:
            file_handler = filehandler.init(self.file_path)
            tasks = TaskManager(file_handler)
            self.ui.main_menu()
        except UnsupportedFileFormat as e:
            self.ui.file_format_error(e)
