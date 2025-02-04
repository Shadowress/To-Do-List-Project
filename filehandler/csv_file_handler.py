import csv
from datetime import datetime
from typing import TYPE_CHECKING

from common.exceptions import FileDataError, CSVParsingError, FileWriteError
from entities import Task
from entities.task_status import TaskStatus
from .file_handler import FileHandler

if TYPE_CHECKING:
    from services import TaskManager


class CSVFileHandler(FileHandler):
    comma_token: str = "###COMMA###"

    def load_file(self, data_storage: 'TaskManager') -> None:
        try:
            with open(self.file_path, "r") as file:
                reader = csv.reader(file)
                next(reader)

                comma_token: str = self.comma_token
                for line_number, line in enumerate(reader, start=2):
                    try:
                        task_id = int(line[0])
                        title = line[1].replace(comma_token, ",")
                        description = line[2].replace(comma_token, ",")
                        due_date = datetime.strptime(line[3], data_storage.date_format)
                        status = TaskStatus(line[4])

                        data_storage.add_task_to_storage(Task(task_id, title, description, due_date, status))
                    except (ValueError, IndexError) as e:
                        raise FileDataError(f"Error on line {line_number}: {line} - {str(e)}")
        except csv.Error as e:
            raise CSVParsingError(f"CSV Parsing Error: {str(e)}")

    def write_file(self, data_storage: 'TaskManager') -> None:
        try:
            with open(self.file_path, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["task_id", "title", "description", "due_date", "status"])

                comma_token: str = self.comma_token
                for task in data_storage.task_storage:
                    try:
                        data: list = [
                            task.task_id,
                            task.title.replace(",", comma_token),
                            task.description.replace(",", comma_token),
                            task.due_date.strftime(data_storage.date_format),
                            task.status.value
                        ]

                        writer.writerow(data)
                    except ValueError as e:
                        raise FileWriteError(f"Error writing data for task ID {task.task_id}: {str(e)}")
        except csv.Error as e:
            raise CSVParsingError(f"CSV Parsing Error: {str(e)}")

    def append_file(self, data_storage: 'TaskManager', task: 'Task') -> None:
        try:
            with open(self.file_path, "a", newline="") as file:
                writer = csv.writer(file)

                comma_token: str = self.comma_token
                try:
                    data: list = [
                        task.task_id,
                        task.title.replace(",", comma_token),
                        task.description.replace(",", comma_token),
                        task.due_date.strftime(data_storage.date_format),
                        task.status.value
                    ]

                    writer.writerow(data)
                except ValueError as e:
                    raise FileWriteError(f"Error writing data for task ID {task.task_id}: {str(e)}")
        except csv.Error as e:
            raise CSVParsingError(f"CSV Parsing Error: {str(e)}")
