import csv
from dataclasses import fields
from datetime import datetime
from typing import TYPE_CHECKING

from common.exceptions import FileDataError, CSVParsingError
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
                        due_date = datetime.strptime(line[3], "%Y-%m-%d")
                        status = TaskStatus(line[4])

                        data_storage.add_task_to_storage(Task(task_id, title, description, due_date, status))
                    except (ValueError, IndexError) as e:
                        raise FileDataError(f"Error on line {line_number}: {line} - {str(e)}")
        except csv.Error as e:
            raise CSVParsingError(f"CSV Parsing Error: {str(e)}")

    # todo test
    def write_file(self, data_storage: 'TaskManager') -> None:
        try:
            with open(self.file_path, "w", newline="") as file:
                writer = csv.writer(file)

                # noinspection PyTypeChecker
                writer.writerow([field.name for field in fields(Task)])

                comma_token: str = self.comma_token
                # todo Note: task_data is a Task object
                for task_data in data_storage.task_storage:
                    row = ",".join([data.replace(",", comma_token) for data in task_data])
                    writer.writerow(row)

        except csv.Error as e:
            raise CSVParsingError(f"CSV Parsing Error: {str(e)}")

    # todo test
    def append_file(self, data_storage: 'TaskManager', new_data: 'Task') -> None:
        try:
            with open(self.file_path, "a", newline="") as file:
                writer = csv.writer(file)

                comma_token: str = self.comma_token
                row = ",".join([data.replace(",", comma_token) for data in new_data])
                writer.writerow(row)

        except csv.Error as e:
            raise CSVParsingError(f"CSV Parsing Error: {str(e)}")
