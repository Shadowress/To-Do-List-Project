from datetime import datetime
from pathlib import Path
from typing import TYPE_CHECKING

from common.exceptions import UnsupportedFileFormatError, InvalidUIError, InvalidDisplayDateFormatError
from filehandler.csv_file_handler import CSVFileHandler
from filehandler.json_file_handler import JSONFileHandler
from ui.console_menu import ConsoleMenu

if TYPE_CHECKING:
    from filehandler import FileHandler
    from ui import UI


def create_ui(ui: str) -> 'UI':
    try:
        # Add new ui below if new ui is added
        match ui:
            case "console menu":
                return ConsoleMenu()
            case _:
                raise InvalidUIError(f"Invalid UI Provided: {ui}")

    except InvalidUIError as e:
        # The default ui selection can be changed below
        default_ui_selection: str = "console menu"
        default_ui: 'UI' = create_ui(default_ui_selection)

        default_ui.display_error(e)
        default_ui.display_message(f"Proceeded using default ui: {default_ui_selection}")

        return default_ui


def create_file_handler(file_path: str, ui: 'UI') -> 'FileHandler':
    try:
        file_path = "data/" + file_path
        file_format = _get_file_format(file_path)

        # Add new file_format below if new file handler is added
        match file_format:
            case "csv" | "txt":
                return CSVFileHandler(file_path)
            case "json":
                return JSONFileHandler(file_path)
            case _:
                raise UnsupportedFileFormatError(f"Unsupported file format: {file_format}")

    except UnsupportedFileFormatError as e:
        # The default file path and file handler can be changed below
        default_file_path: str = "task.csv"
        default_file_handler: 'FileHandler' = CSVFileHandler(default_file_path)

        ui.display_error(e)
        ui.display_message(f"Proceeded using default file path: {default_file_path}")

        return default_file_handler


def _get_file_format(file_path: str) -> str:
    return Path(file_path).suffix.lstrip(".")


def set_display_date_format(date_format: str, ui: 'UI') -> str:
    try:
        if _is_valid_date_format(date_format):
            return date_format
        else:
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
