from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

import config
from common.factory import set_display_date_format

if TYPE_CHECKING:
    from controller import Controller


class UI(ABC):
    def __init__(self) -> None:
        self.display_date_format = set_display_date_format(config.DISPLAY_DATE_FORMAT)

    @abstractmethod
    def run_main_menu(self, controller: 'Controller') -> None:
        ...

    @abstractmethod
    def display_message(self, message: str) -> None:
        ...

    @abstractmethod
    def display_error(self, exception: Exception) -> None:
        ...

    @abstractmethod
    def display_error_and_exit(self, exception: Exception) -> None:
        ...
