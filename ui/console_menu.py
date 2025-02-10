import sys

from .ui import UI


class ConsoleMenu(UI):
    @staticmethod
    def _display_main_menu() -> None:
        print("""
--------------------------------------------------
              To-Do-List Application
    1) View Tasks
    2) Add Tasks
    3) Edit Tasks
    4) Delete Tasks
    5) Exit System
--------------------------------------------------
""")

    @staticmethod
    def _display_view_menu() -> None:
        print("""
--------------------------------------------------
                    View Menu
    1) Display All Tasks
    2) Display Tasks Filtered By Title
    3) Display Tasks Filtered By Status
    4) Return To Main Menu
--------------------------------------------------
""")

    @staticmethod
    def _display_edit_menu() -> None:
        print("""
--------------------------------------------------
                    Edit Menu
    1) Edit Task Details
    2) Update Task Status
    3) Return To Main Menu
--------------------------------------------------
""")

    @staticmethod
    def _display_tasks(tasks: tuple[dict[str, str], ...], display_index: bool = False):
        print("--------------------------------------------------")

        for index, task in enumerate(tasks, start=1):
            print(f"""{f"\n    Index: {index}" if display_index else ""}
    Title: {task["title"]}
    Description: {task["description"]}
    Due Date: {task["due_date"]}
    Task Status: {task["status"]}
""")

        print("--------------------------------------------------")

    @staticmethod
    def _get_menu_selection() -> str:
        return input("Please enter a selection: ").strip()

    def display_message(self, message: str) -> None:
        print(message)

    def display_error(self, exception: Exception) -> None:
        print(exception)

    def display_error_and_exit(self, exception: Exception) -> None:
        print(exception)
        sys.exit(1)

    def _process_main(self) -> None:
        while True:
            ConsoleMenu._display_main_menu()

            match ConsoleMenu._get_menu_selection():
                case "1":
                    self._process_view_tasks()
                case "2":
                    self._process_add_task()
                case "3":
                    self._process_edit_task()
                case "4":
                    self._process_delete_task()
                case "5":
                    break
                case _:
                    print("Please enter a valid selection! (1 - 3)")

    def _process_view_tasks(self) -> None:
        while True:
            ConsoleMenu._display_view_menu()

            match ConsoleMenu._get_menu_selection():
                case "1":
                    ConsoleMenu._display_tasks(self._get_formatted_tasks_for_display())
                case "2":
                    self._process_task_filter_by_title()
                case "3":
                    ...  # todo add filter view by status
                case "4":
                    break
                case _:
                    print("Please enter a valid selection! (1 - 3)")

    def _process_task_filter_by_title(self) -> None:
        title_filter = input("Please enter a title that you want to search by: ").strip()
        tasks: tuple[dict[str, str], ...] = self._get_formatted_tasks_for_display(title_filter)
        ConsoleMenu._display_tasks(tasks)

    def _process_add_task(self) -> None:
        ...

    def _process_edit_task(self) -> None:
        while True:
            ConsoleMenu._display_edit_menu()

            match ConsoleMenu._get_menu_selection():
                case "1":
                    ...
                case "2":
                    ...
                case "3":
                    break
                case _:
                    print("Please enter a valid selection! (1 - 3)")

    def _process_edit_task_details(self) -> None:
        tasks: tuple[dict[str, str], ...] = self._get_formatted_tasks_for_display()
        ConsoleMenu._display_tasks(tasks, True)

    def _process_update_task_status(self) -> None:
        # todo get Pending, In Progress, and Overdue only
        tasks: tuple[dict[str, str], ...] = self._get_formatted_tasks_for_display()
        ConsoleMenu._display_tasks(tasks, True)

    def _process_delete_task(self) -> None:
        ...
