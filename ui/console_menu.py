import sys
from typing import TYPE_CHECKING

from .ui import UI

if TYPE_CHECKING:
    pass


class ConsoleMenu(UI):
    def run_main_menu(self) -> None:
        self._display_main_menu()
        selection = input("Please enter a selection: ").strip()

        match selection:
            case "1":
                self.display_view_menu()
            case "2":
                self._display_add_menu()
            case "3":
                self._display_edit_menu()
            case "4":
                ...
            case "5":
                ...

    def display_message(self, message: str) -> None:
        print(message)

    def display_error(self, exception: Exception) -> None:
        print(exception)

    def display_error_and_exit(self, exception: Exception) -> None:
        print(exception)
        sys.exit(1)

    def _display_main_menu(self) -> None:
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

    def display_view_menu(self) -> None:
        ...

    def _display_add_menu(self) -> None:
        ...

    def _display_edit_menu(self) -> None:
        ...
