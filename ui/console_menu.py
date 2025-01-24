from .ui import UI
import sys


class ConsoleMenu(UI):

    def main_menu(self) -> None:
        print()

    def file_path_error(file_format: str) -> None:
        print(f"Failed to connect to system: {file_format} files are not accepted by this program")
        sys.exit()