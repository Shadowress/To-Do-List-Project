import sys
from typing import TYPE_CHECKING

from .ui import UI

if TYPE_CHECKING:
    from controller import Controller


class ConsoleMenu(UI):
    def run_main_menu(self, controller: 'Controller') -> None:
        ...

    def display_message(self, message: str) -> None:
        print(message)

    def display_error(self, exception: Exception) -> None:
        print(exception)

    def display_error_and_exit(self, exception: Exception) -> None:
        print(exception)
        sys.exit(1)
