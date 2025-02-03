from common.exceptions import InvalidUIError
from ui.console_menu import ConsoleMenu
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ui import UI

def init(ui_selection: str) -> None:
    match ui_selection:
        case "console menu":
            ui: UI = ConsoleMenu()
        case _:
            # todo prompt invalid ui
            ui: UI = ConsoleMenu()  # default ui
            raise InvalidUIError(f"Invalid UI Provided: {ui_selection}")