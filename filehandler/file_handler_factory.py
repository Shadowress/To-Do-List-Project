from pathlib import Path

from common.exceptions import UnsupportedFileFormat
from .csv_file_handler import CSVFileHandler
from .file_handler import FileHandler
from .json_file_handler import JSONFileHandler


# todo do data loading on sep thread
# todo add checking when needing to write to file
def init(file_path: str) -> FileHandler:
    file_format = get_file_format(file_path)

    # Add new file_format below if new file handler is added
    match file_format:
        case "csv":
            return CSVFileHandler(file_path)
        case "json":
            return JSONFileHandler(file_path)
        case _:
            raise UnsupportedFileFormat(file_format)


def get_file_format(file_path: str) -> str:
    return Path(file_path).suffix.lstrip(".")
