from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

import config
from common.factory import set_display_date_format

if TYPE_CHECKING:
    from controller import Controller


class UI(ABC):
    DISPLAY_DATE_FORMAT: str

    def __init__(self, controller: 'Controller') -> None:  # todo
        UI.DISPLAY_DATE_FORMAT = set_display_date_format(config.DISPLAY_DATE_FORMAT, self)
        self.controller: 'Controller' = controller

    @staticmethod
    @abstractmethod
    def run_main_menu(self) -> None:
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
