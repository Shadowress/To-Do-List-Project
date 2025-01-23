from filehandler import file_handler
from services import TaskManager


def main() -> None:
    file_path = "task."  # Both csv and json
    tasks = TaskManager(file_handler)
    menu.main_menu()


if __name__ == "__main__":
    main()
