from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from controller import Controller


class UI(ABC):
    @abstractmethod
    def run_main_menu(self, controller: 'Controller') -> None:
        ...

    @abstractmethod
    def display_error(self, exception: Exception) -> None:
        ...

    @abstractmethod
    def display_error_and_exit(self, exception: Exception) -> None:
        ...
