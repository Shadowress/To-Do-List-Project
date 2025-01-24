from abc import ABC, abstractmethod


class FileHandler(ABC):

    def __init__(self, file_path: str):
        self.file_path = file_path

    @abstractmethod
    def load_file(self) -> None:
        ...

    @abstractmethod
    def write_file(self) -> None:
        ...

    @abstractmethod
    def append_file(self) -> None:
        ...
