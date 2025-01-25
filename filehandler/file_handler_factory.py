import os
from pathlib import Path

from common.exceptions import UnsupportedFileFormat
from .csv_file_handler import CSVFileHandler
from .file_handler import FileHandler
from .json_file_handler import JSONFileHandler


def init(file_path: str) -> FileHandler:
    file_format = _get_file_format(file_path)

    # Add new file_format below if new file handler is added
    match file_format:
        case "csv":
            if not os.path.exists(file_path):
                open(file_path, "x").close()
            return CSVFileHandler(file_path)

        case "json":
            if not os.path.exists(file_path):
                open(file_path, "x").close()
            return JSONFileHandler(file_path)

        case _:
            raise UnsupportedFileFormat(file_format)


def _get_file_format(file_path: str) -> str:
    return Path(file_path).suffix.lstrip(".")
