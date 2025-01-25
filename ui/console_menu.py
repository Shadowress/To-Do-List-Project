import sys

from common.exceptions import UnsupportedFileFormat
from .ui import UI


class ConsoleMenu(UI):

    def main_menu(self) -> None:
        print()

    def file_format_error(self, exception: UnsupportedFileFormat) -> None:
        print(exception)
        sys.exit()
