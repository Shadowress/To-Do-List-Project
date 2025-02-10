from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

import config
from common.factory import set_display_date_format

if TYPE_CHECKING:
    from controller import Controller
    from entities import Task


class UI(ABC):
    _DISPLAY_DATE_FORMAT: str

    def __init__(self, controller: 'Controller') -> None:
        UI._DISPLAY_DATE_FORMAT = set_display_date_format(config.DISPLAY_DATE_FORMAT, self)
        self.controller: 'Controller' = controller

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
    def _process_main(self) -> None:
        pass

    @classmethod
    def _get_display_date_format(cls) -> str:
        return cls._DISPLAY_DATE_FORMAT

    def run(self) -> None:
        self._process_main()

    def _get_formatted_tasks_for_display(self, title_filter: str = None) -> tuple[dict[str, str], ...]:
        if title_filter:
            tasks: tuple['Task', ...] = self.controller.get_tasks_by_title(title_filter)
        else:
            tasks: tuple['Task', ...] = self.controller.get_all_tasks()

        return tuple(
            {
                "title": task.title,
                "description": task.description,
                "due_date": task.due_date.strftime(UI._get_display_date_format()),
                "status": task.status
            }
            for task in tasks
        )
