import sys
from typing import TYPE_CHECKING

from .ui import UI

if TYPE_CHECKING:
    pass


class ConsoleMenu(UI):
    def run_main_menu(self) -> None:
        print("""
--------------------------------------------------
              To-Do-List Application
    1) View To-Do-List
    2) Add Task
    3) Edit Task
    4) Delete Task
    5) Exit System
--------------------------------------------------
""")
        selection = input("Please enter a selection: ").strip()

        match selection:
            case "1":
                ...
            case "2":
                ...

    def display_message(self, message: str) -> None:
        print(message)

    def display_error(self, exception: Exception) -> None:
        print(exception)

    def display_error_and_exit(self, exception: Exception) -> None:
        print(exception)
        sys.exit(1)

    def main_menu(self) -> None:
        print("""
--------------------------------------------------
              To-Do-List Application
    1) View To-Do-List
    2) Add Task
    3) Edit Task
    4) Delete Task
    5) Exit System
--------------------------------------------------
""")
