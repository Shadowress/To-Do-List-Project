from filehandler import FileHandler
from services import TaskManager
from ui import console_menu


def main() -> None:
    # File path and file format can be changed
    file_path = "task.csv"

    tasks = TaskManager(FileHandler(file_path))

    # Preferred UI can be changed
    console_menu.main_menu()



if __name__ == "__main__":
    main()
