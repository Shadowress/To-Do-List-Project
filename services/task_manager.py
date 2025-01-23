from filehandler import FileHandler
from entities import Task


class TaskManager:

    def __init__(self, file_handler: FileHandler) -> None:
        self.file_handler = file_handler

    def add_task(self) -> None:
        ...

    def delete_task(self) -> None:
        ...

    def edit_task(self) -> None:
        ...

    def find_task_by_title(self) -> Task:
        ...
