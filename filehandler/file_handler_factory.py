from pathlib import Path
from typing import TYPE_CHECKING

from .csv_file_handler import CSVFileHandler
from .json_file_handler import JSONFileHandler

if TYPE_CHECKING:
    from .file_handler import FileHandler


def init(file_path: str) -> 'FileHandler':
    file_format = _get_file_format(file_path)

    # Add new file_format below if new file handler is added
    match file_format:
        case "csv":
            return CSVFileHandler(file_path)
        case "json":
            return JSONFileHandler(file_path)
        case _:
            # todo change the Exception
            raise Exception(f"Unsupported file format: {file_format}")


def _get_file_format(file_path: str) -> str:
    return Path(file_path).suffix.lstrip(".")
