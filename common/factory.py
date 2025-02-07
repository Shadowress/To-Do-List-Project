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
        try:
            ui_type: 'UIType' = UIType(ui_selection)
        except ValueError:
            raise InvalidUIError(f"Invalid ui provided: {ui_selection}")

        ui_class: type = _get_ui(ui_type)
        ui: 'UI' = ui_class(controller)
        return ui

    except (InvalidUIError, UITypeMappingError) as e:
        return _handle_fallback_ui(controller, e)


def _handle_fallback_ui(controller: 'Controller', exception: Exception) -> 'UI':
    # The default ui selection can be changed below
    default_ui_selection: 'UIType' = UIType.CONSOLE_MENU

    default_ui_class: type = _get_ui(default_ui_selection)
    default_ui: 'UI' = default_ui_class(controller)

    default_ui.display_error(exception)
    default_ui.display_message(f"Proceeded using default ui: {default_ui_selection.value}")

    return default_ui


def _get_file_handler(file_format: str) -> type:
    from filehandler.csv_file_handler import CSVFileHandler
    from filehandler.json_file_handler import JSONFileHandler

    # Add new file format mapping below if new file format is added
    file_format_mapping: dict[str, type] = {
        "csv": CSVFileHandler,
        "txt": CSVFileHandler,
        "json": JSONFileHandler
    }

    if file_format not in file_format_mapping:
        raise UnsupportedFileFormatError(f"Unsupported file format: {file_format}")

    return file_format_mapping[file_format]


def create_file_handler(ui: 'UI') -> 'FileHandler':
    try:
        file_path: str = config.FILE_PATH
        file_format: str = _get_file_format(file_path)
        file_handler_class: type = _get_file_handler(file_format)
        file_handler: 'FileHandler' = file_handler_class(file_path)
        return file_handler

    except UnsupportedFileFormatError as e:
        return _handle_fallback_file_handler(ui, e)


def _get_file_format(file_path: str) -> str:
    return Path(file_path).suffix.lstrip(".")


def _handle_fallback_file_handler(ui: 'UI', exception: Exception) -> 'FileHandler':
    # The default file path can be changed below
    default_file_path: str = "task.csv"

    default_file_format: str = _get_file_format(default_file_path)
    default_file_handler_class: type = _get_file_handler(default_file_format)
    default_file_handler: 'FileHandler' = default_file_handler_class(default_file_path)

    ui.display_error(exception)
    ui.display_message(f"Proceeded using default file path: {default_file_path}")

    return default_file_handler


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

        # Checks if there is an extra time component
        return parsed_date.strftime(date_format) == test_date

    except ValueError:
        return False
