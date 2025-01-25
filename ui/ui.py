from abc import ABC, abstractmethod

from common.exceptions import UnsupportedFileFormat


class UI(ABC):

    @abstractmethod
    def main_menu(self) -> None:
        ...

    @abstractmethod
    def file_format_error(self, exception: UnsupportedFileFormat) -> None:
        ...