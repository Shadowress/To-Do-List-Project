from datetime import datetime
from enum import Enum
from pathlib import Path
from typing import TYPE_CHECKING

import config
from common.exceptions import UnsupportedFileFormatError, InvalidUIError, InvalidDisplayDateFormatError, \
    UITypeMappingError

if TYPE_CHECKING:
    from filehandler import FileHandler
    from ui import UI
    from controller import Controller


class UIType(Enum):
    # Add new ui type below if new ui is added
    CONSOLE_MENU: str = "console menu"


def _get_ui(ui_type: 'UIType') -> type:
    from ui.console_menu import ConsoleMenu

    # Add new ui mapping below if new ui is added
    ui_mapping: dict['Enum', type] = {
        UIType.CONSOLE_MENU: ConsoleMenu
    }

    if ui_type not in ui_mapping:
        raise UITypeMappingError(f"UIType mapping not found: {ui_type.value}")

    return ui_mapping[ui_type]


def create_ui(controller: 'Controller') -> 'UI':
    ui_selection: str = config.UI.lower().strip()

    try:
        ui_type: 'UIType' = UIType(ui_selection)
        ui_class: type = _get_ui(ui_type)

        return ui_class(controller)

    except ValueError:
        raise InvalidUIError(f"Invalid ui provided: {ui_selection}")

    # todo debug: except block is not called when exception raised
    except (InvalidUIError, UITypeMappingError) as e:
        # The default ui selection can be changed below
        default_ui_selection: 'UIType' = UIType.CONSOLE_MENU

        ui_class: type = _get_ui(default_ui_selection)
        ui = ui_class(controller)

        ui.display_error(e)
        ui.display_message(f"Proceeded using default ui: {default_ui_selection.value}")

        return ui


# todo refactor
def create_file_handler(ui: 'UI') -> 'FileHandler':
    try:
        file_path = "data/" + config.FILE_PATH
        file_format = _get_file_format(file_path)

        # Add new file_format below if new file handler is added
        match file_format:
            case "csv" | "txt":
                from filehandler.csv_file_handler import CSVFileHandler
                return CSVFileHandler(file_path)
            case "json":
                from filehandler.json_file_handler import JSONFileHandler
                return JSONFileHandler(file_path)
            case _:
                raise UnsupportedFileFormatError(f"Unsupported file format: {file_format}")

    except UnsupportedFileFormatError as e:
        # The default file path and file handler can be changed below
        default_file_path: str = "task.csv"
        default_file_handler: 'FileHandler' = create_file_handler(ui)

        ui.display_error(e)
        ui.display_message(f"Proceeded using default file path: {default_file_path}")

        return default_file_handler


def _get_file_format(file_path: str) -> str:
    return Path(file_path).suffix.lstrip(".")


def set_display_date_format(date_format: str, ui: 'UI') -> str:
    try:
        if _is_valid_date_format(date_format):
            return date_format

        raise InvalidDisplayDateFormatError(f"Invalid Display Date Format Provided: {date_format}")

    except InvalidDisplayDateFormatError as e:
        # The default display date format can be changed below
        default_display_date_format: str = "%Y-%m-%d"

        ui.display_error(e)
        ui.display_message(f"Proceeded using default display date format: {default_display_date_format}")

        return default_display_date_format


def _is_valid_date_format(date_format: str) -> bool:
    try:
        test_date: str = "2000-01-01"
        parsed_date: 'datetime' = datetime.strptime(test_date, date_format)

        # Check if there is an extra time component
        return parsed_date.strftime(date_format) == test_date

    except ValueError:
        return False
