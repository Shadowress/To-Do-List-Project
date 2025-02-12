from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Union

import config
from common.factory import set_display_date_format

if TYPE_CHECKING:
    from controller import Controller
    from entities import Task


class UI(ABC):
    _DISPLAY_DATE_FORMAT: str

    def __init__(self, controller: 'Controller') -> None:
        UI._DISPLAY_DATE_FORMAT = set_display_date_format(config.DISPLAY_DATE_FORMAT, self)
        self._controller: 'Controller' = controller

    @abstractmethod
    def run(self) -> None:
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

    @classmethod
    def _get_display_date_format(cls) -> str:
        return cls._DISPLAY_DATE_FORMAT

    def _get_formatted_tasks_for_display(
            self,
            title_filter: str = None,
            status_filter: str = None
    ) -> tuple[dict[str, Union[int, str]], ...]:
        if title_filter:
            tasks: tuple['Task', ...] = self._controller.get_tasks_by_title(title_filter)
        elif status_filter:
            tasks: tuple['Task', ...] = self._controller.get_tasks_by_status(status_filter)
        else:
            tasks: tuple['Task', ...] = self._controller.get_all_tasks()

        return tuple(
            {
                "task_id": task.task_id,
                "title": task.title,
                "description": task.description,
                "due_date": task.due_date.strftime(UI._get_display_date_format()),
                "status": task.status
            }
            for task in tasks
        )
