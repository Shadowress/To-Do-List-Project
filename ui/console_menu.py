import sys
from datetime import datetime
from typing import Union

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
    def _display_edit_task_details_menu() -> None:
        print("""
--------------------------------------------------
              Edit Task Details Menu
    1) Edit All Task Details
    2) Edit Task Title
    3) Edit Task Description
    4) Edit Task Due Date
    5) Return To Edit Menu
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

    @staticmethod
    def _get_user_input(prompt: str) -> str:
        while True:
            user_input = input(prompt).strip()

            if user_input:
                return user_input

    @staticmethod
    def _get_user_date_input(
            prompt: str,
            error_message: str,
            return_type: type[Union[str, 'datetime']] = datetime
    ) -> Union[str, 'datetime']:
        date_format: str = ConsoleMenu._get_display_date_format()

        while True:
            try:
                due_date_input: str = input(prompt).strip()
                due_date: 'datetime' = datetime.strptime(due_date_input, date_format)

                return due_date_input if return_type is str else due_date

            except ValueError:
                print(error_message)

    def run(self) -> None:
        self._process_main_menu()

    def display_message(self, message: str) -> None:
        print(message)

    def display_error(self, exception: Exception) -> None:
        print(exception)

    def display_error_and_exit(self, exception: Exception) -> None:
        print(exception)
        sys.exit(1)

    def _process_main_menu(self) -> None:
        while True:
            ConsoleMenu._display_main_menu()

            match ConsoleMenu._get_menu_selection():
                case "1":
                    self._process_view_tasks_menu()
                case "2":
                    self._process_add_task_menu()
                case "3":
                    self._process_edit_task_menu()
                case "4":
                    self._process_delete_task()
                case "5":
                    break
                case _:
                    print("Please enter a valid selection! (1 - 3)")

    def _process_view_tasks_menu(self) -> None:
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
        title_filter: str = input("Please enter a title that you want to search by: ").strip()
        tasks: tuple[dict[str, str], ...] = self._get_formatted_tasks_for_display(title_filter)
        ConsoleMenu._display_tasks(tasks)

    def _process_add_task_menu(self) -> None:
        date_format: str = ConsoleMenu._get_display_date_format()
        new_task_data: dict[str, Union[str, 'datetime']] = {
            "title": ConsoleMenu._get_user_input("Please enter a title for the new task: "),
            "description": ConsoleMenu._get_user_input("Please enter a description for the new task: "),
            "due_date": ConsoleMenu._get_user_date_input(
                f"Please enter a due date for the new task ({date_format}): ",
                f"Please enter a valid date with the date format: {date_format}")
        }
        self._controller.add_task(new_task_data)

    def _process_edit_task_menu(self) -> None:
        while True:
            ConsoleMenu._display_edit_menu()

            match ConsoleMenu._get_menu_selection():
                case "1":
                    self._process_edit_task_details_menu()
                case "2":
                    self._process_update_task_status()
                case "3":
                    break
                case _:
                    print("Please enter a valid selection! (1 - 3)")

    def _get_task_by_index(self) -> dict[str, str]:
        tasks: tuple[dict[str, str], ...] = self._get_formatted_tasks_for_display()
        ConsoleMenu._display_tasks(tasks, True)

        while True:
            try:
                task_index: int = int(
                    input("Please enter the index of the task that you would like to edit: ").strip()) - 1
                task: dict[str, str] = tasks[task_index]
                return task

            except (ValueError, IndexError):
                print("Please enter a valid task index!")

    def _process_edit_task_details_menu(self) -> None:
        task: dict[str, str] = self._get_task_by_index()

        while True:
            ConsoleMenu._display_edit_task_details_menu()

            match ConsoleMenu._get_menu_selection():
                case "1":
                    self._process_edit_task_details(task, "all")
                case "2":
                    self._process_edit_task_details(task, "title")
                case "3":
                    self._process_edit_task_details(task, "description")
                case "4":
                    self._process_edit_task_details(task, "due_date")
                case "5":
                    break
                case _:
                    print("Please enter a valid selection! (1 - 5)")

        # todo

    def _process_edit_task_details(self, task: dict[str, str], field_to_edit: str):
        new_task_data: dict[str, Union[str, 'datetime']] = task

        if field_to_edit in {"title", "all"}:
            new_task_data["title"] = self._get_user_input("Please enter a new title: ")

        if field_to_edit in {"description", "all"}:
            new_task_data["description"] = self._get_user_input("Please enter a new description: ")

        if field_to_edit in {"due_date", "all"}:
            date_format: str = ConsoleMenu._get_display_date_format()
            new_task_data["due_date"] = self._get_user_date_input(
                f"Please enter a new due date ({date_format}): ",
                f"Please enter a valid date with the date format: {date_format}",
                return_type=str)  # todo currently using date format of ui

    def _process_update_task_status(self) -> None:
        # todo get Pending, In Progress, and Overdue only
        tasks: tuple[dict[str, str], ...] = self._get_formatted_tasks_for_display()
        ConsoleMenu._display_tasks(tasks, True)

        # todo

    def _process_delete_task(self) -> None:
        tasks: tuple[dict[str, str], ...] = self._get_formatted_tasks_for_display()
        ConsoleMenu._display_tasks(tasks, True)

        # todo del task by index
