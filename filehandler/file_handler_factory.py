from pathlib import Path

from .file_handler import FileHandler


def init(file_path: str) -> FileHandler:
    ...


def get_file_format(file_path: str) -> str:
    return Path(file_path).suffix.lstrip(".")
