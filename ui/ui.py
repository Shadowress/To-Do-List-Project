from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

import config
from common.factory import set_display_date_format

if TYPE_CHECKING:
    from controller import Controller
    from entities import Task


class UI(ABC):
    DISPLAY_DATE_FORMAT: str

    def __init__(self, controller: 'Controller') -> None:
        UI.DISPLAY_DATE_FORMAT = set_display_date_format(config.DISPLAY_DATE_FORMAT, self)
        self.controller: 'Controller' = controller

    @abstractmethod
    def run_main_menu(self) -> None:
        pass

    @abstractmethod
    def display_message(self, message: str) -> None:
        pass

    @abstractmethod
    def display_error(self, exception: Exception) -> None:
        pass

    @abstractmethod
    def display_error_and_exit(self, exception: Exception) -> None:
        pass

    @abstractmethod
    def _display_main_menu(self) -> None:
        pass

    @abstractmethod
    def _display_add_menu(self) -> None:
        pass

    @abstractmethod
    def _display_edit_menu(self) -> None:
        pass

    def _get_formatted_tasks_for_display(self) -> tuple[dict[str, str], ...]:
        tasks: tuple['Task', ...] = self.controller.get_tasks()

        return tuple(
            {
                "title": task.title,
                "description": task.description,
                "due_date": task.due_date.strftime(UI.DISPLAY_DATE_FORMAT),
                "status": task.status
            }
            for task in tasks
        )
