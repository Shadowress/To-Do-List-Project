import filehandler
from services import TaskManager
from ui import console_menu


def main() -> None:
    # File path and file format can be changed
    file_path = "task.csv"

    file_handler = filehandler.init(file_path)
    tasks = TaskManager(file_handler)

    # Preferred UI can be changed
    console_menu.main_menu()


if __name__ == "__main__":
    main()
