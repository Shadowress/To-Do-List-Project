from abc import ABC, abstractmethod


class UI(ABC):

    @abstractmethod
    def main_menu(self) -> None:
        ...
