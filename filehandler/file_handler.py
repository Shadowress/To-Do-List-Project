from abc import ABC, abstractmethod
from pathlib import Path


class FileHandler(ABC):

    def __init__(self, file_path: str):
        # todo add checking for the file path

        self.file_path = file_path

    @staticmethod
    def get_file_format(file_path: str) -> str:
        return Path(file_path).suffix.lstrip(".")

    @abstractmethod
    def load_file(self) -> None:
        ...

    @abstractmethod
    def write_file(self) -> None:
        ...

    @abstractmethod
    def append_file(self) -> None:
        ...
