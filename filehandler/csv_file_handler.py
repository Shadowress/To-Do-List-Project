import csv
from datetime import datetime
from typing import TYPE_CHECKING

from entities import Task
from entities.task_status import TaskStatus
from .file_handler import FileHandler

if TYPE_CHECKING:
    from services import TaskManager


class CSVFileHandler(FileHandler):

    def load_file(self, data_storage: 'TaskManager') -> None:
        try:
            with open(self.file_path, 'r') as file:
                reader = csv.reader(file)
                next(reader)
                for line in reader:
                    task_id = int(line[0])
                    title = line[1]
                    description = line[2]
                    due_date = datetime.strptime(line[3], "%Y-%m-%d")
                    status = TaskStatus(line[4])

                    data_storage.add_task_to_storage(Task(task_id, title, description, due_date, status))
        except csv.Error as e:
            ...  # todo

    def write_file(self) -> None:
        pass

    def append_file(self) -> None:
        pass
