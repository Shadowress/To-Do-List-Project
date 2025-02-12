import sys
from datetime import datetime
from typing import Union

from entities.task_status import TaskStatus
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
    def _display_edit_changes(
            original_task_data: dict[str, Union[str, 'datetime']],
            new_task_data: dict[str, Union[str, 'datetime']]
    ) -> None:
        def format_change(field: str) -> str:
            old_value = original_task_data[field]
            new_value = new_task_data.get(field, old_value)

            if isinstance(old_value, datetime):
                old_value = old_value.strftime(ConsoleMenu._get_display_date_format())
            if isinstance(new_value, datetime):
                new_value = new_value.strftime(ConsoleMenu._get_display_date_format())

            return f"{old_value} -> {new_value}" if old_value != new_value else str(old_value)

        print(f"""
--------------------------------------------------

    Title: {format_change("title")}
    Description: {format_change("description")}
    Due Date: {format_change("due_date")}
    Task Status: {format_change("status")}

--------------------------------------------------
""")

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
    def _get_user_confirmation(prompt: str) -> bool:
        while True:
            confirmation: str = input(prompt).strip().lower()

            match confirmation:
                case "yes":
                    return True
                case "no":
                    return False
                case _:
                    print("Please enter yes / no!")

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
                    self._process_filter_task_by_title()
                case "3":
                    self._process_filter_task_by_status()
                case "4":
                    break
                case _:
                    print("Please enter a valid selection! (1 - 3)")

    def _process_filter_task_by_title(self) -> None:
        title_filter: str = input("Please enter a title that you want to search by: ").strip()
        tasks: tuple[dict[str, Union[int, str]], ...] = self._get_formatted_tasks_for_display(title_filter=title_filter)
        ConsoleMenu._display_tasks(tasks)

    def _process_filter_task_by_status(self) -> None:
        while True:
            print(f"Available status: {", ".join(status.value for status in TaskStatus)}")
            status_filter: str = input("Please enter a status that you want to search by: ").strip().capitalize()

            if status_filter in TaskStatus.__members__.values():
                break

            self.display_message("Please enter a valid status!")

        tasks: tuple[dict[str, Union[int, str]], ...] = self._get_formatted_tasks_for_display(
            status_filter=status_filter)
        ConsoleMenu._display_tasks(tasks)

    def _process_add_task_menu(self) -> None:
        date_format: str = ConsoleMenu._get_display_date_format()
        new_task_data: dict[str, Union[str, 'datetime']] = {
            "title": ConsoleMenu._get_user_input("Please enter a title for the new task: "),
            "description": ConsoleMenu._get_user_input("Please enter a description for the new task: "),
            "due_date": self._get_user_date_input(
                f"Please enter a due date for the new task ({date_format}): ",
                f"Please enter a valid date with the date format: {date_format}")
        }
        self._controller.add_task(new_task_data)

    def _get_user_date_input(self, prompt: str, error_message: str) -> 'datetime':
        date_format: str = ConsoleMenu._get_display_date_format()

        while True:
            try:
                due_date_input: str = input(prompt).strip()
                due_date: 'datetime' = datetime.strptime(due_date_input, date_format)

                if datetime.now() > due_date:
                    self.display_message("The date given cannot be in the past!")

                return due_date

            except ValueError:
                self.display_message(error_message)

    def _process_edit_task_menu(self) -> None:
        task: dict[str, str] = self._get_task_by_index()

        while True:
            ConsoleMenu._display_edit_menu()

            match ConsoleMenu._get_menu_selection():
                case "1":
                    self._process_edit_task_details_menu(task)
                case "2":
                    self._process_update_task_status(task)
                case "3":
                    break
                case _:
                    print("Please enter a valid selection! (1 - 3)")

    def _get_task_by_index(self) -> dict[str, Union[int, str]]:
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

    def _process_edit_task_details_menu(self, task: dict[str, Union[int, str]]) -> None:
        while True:
            ConsoleMenu._display_edit_task_details_menu()

            match ConsoleMenu._get_menu_selection():
                case "1":
                    self._process_edit_task_details(task, "all")
                    break
                case "2":
                    self._process_edit_task_details(task, "title")
                    break
                case "3":
                    self._process_edit_task_details(task, "description")
                    break
                case "4":
                    self._process_edit_task_details(task, "due_date")
                    break
                case "5":
                    break
                case _:
                    print("Please enter a valid selection! (1 - 5)")

    def _process_edit_task_details(self, task: dict[str, Union[int, str]], field_to_edit: str):
        task_id: int = task["task_id"]
        new_task_data: dict[str, Union[str, 'datetime']] = {}

        if field_to_edit in {"title", "all"}:
            new_task_data["title"] = ConsoleMenu._get_user_input("Please enter a new title: ")

        if field_to_edit in {"description", "all"}:
            new_task_data["description"] = ConsoleMenu._get_user_input("Please enter a new description: ")

        if field_to_edit in {"due_date", "all"}:
            date_format: str = ConsoleMenu._get_display_date_format()
            new_task_data["due_date"] = self._get_user_date_input(
                f"Please enter a new due date ({date_format}): ",
                f"Please enter a valid date with the date format: {date_format}")

        ConsoleMenu._display_edit_changes(task, new_task_data)

        if ConsoleMenu._get_user_confirmation("Are you sure you want to update the above (yes / no): "):
            self._controller.edit_task(task_id, new_task_data)

    def _process_update_task_status(self, task: dict[str, Union[int, str]]) -> None:
        status: str = task["status"]

        if status in {TaskStatus.PENDING.value}:
            new_status: str = TaskStatus.IN_PROGRESS.value
        elif status in {TaskStatus.IN_PROGRESS.value, TaskStatus.OVERDUE.value}:
            new_status: str = TaskStatus.COMPLETED.value
        elif status in {TaskStatus.COMPLETED.value}:
            self.display_message("The status of completed tasks cannot be updated!")
            return
        else:
            self.display_error(ValueError(f"The status is not valid: {status}"))
            return

        if ConsoleMenu._get_user_confirmation("Are you sure you want to update the task status above (yes / no): "):
            self._controller.edit_task(task["task_id"], {"status": new_status})

    def _process_delete_task(self) -> None:
        task: dict[str, Union[int, str]] = self._get_task_by_index()
        ConsoleMenu._display_tasks((task,))

        if ConsoleMenu._get_user_confirmation("Are you sure you want to delete the task (yes / no): "):
            self._controller.delete_task(task["task_id"])
