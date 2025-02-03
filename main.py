import config
from controller import Controller
from ui import UI
from ui.console_menu import ConsoleMenu


def main() -> None:
    # File path and file format can be changed in the config.py file
    file_path: str = config.FILE_PATH if config.FILE_PATH else "task.csv"

    # Preferred ui can be changed in the config.py file
    ui: UI
    ui_selection: str = config.UI if config.UI else "console menu"
    match ui_selection:
        case "console menu":
            ui: UI = ConsoleMenu()
        case _:
            ... # todo prompt invalid ui

    Controller(file_path, ui).start()


if __name__ == "__main__":
    main()
