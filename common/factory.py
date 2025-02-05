from datetime import datetime
from pathlib import Path
from typing import TYPE_CHECKING

import config
from common.exceptions import UnsupportedFileFormatError, InvalidUIError, InvalidDisplayDateFormatError

if TYPE_CHECKING:
    from filehandler import FileHandler
    from ui import UI
    from controller import Controller


# todo refactor
def create_ui(controller: 'Controller') -> 'UI':
    from ui.console_menu import ConsoleMenu
    try:
        ui: str = config.UI.lower().strip()

        # Add new ui below if new ui is added
        match ui:
            # todo should i use enum for this?
            case "console menu":
                return ConsoleMenu(controller)
            case _:
                raise InvalidUIError(f"Invalid UI Provided: {ui}")

    except InvalidUIError as e:
        # The default ui selection can be changed below
        default_ui_selection: str = "console menu"
        default_ui: 'UI' = create_ui(controller)

        default_ui.display_error(e)
        default_ui.display_message(f"Proceeded using default ui: {default_ui_selection}")

        return default_ui


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
