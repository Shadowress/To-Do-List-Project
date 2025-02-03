from controller import Controller
from ui.console_menu import ConsoleMenu
from ui import UI


def main() -> None:
    # File path and file format can be changed
    file_path = "task.csv"

    # Preferred ui can be changed
    ui: UI = ConsoleMenu()

    Controller(file_path, ui).start()


if __name__ == "__main__":
    main()
