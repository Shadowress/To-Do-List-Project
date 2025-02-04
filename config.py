# Configuration Settings for the Task Management System

# FILE_PATH: Specify the file name or path for task data storage.
# Supported file formats: "csv", "json", "txt".
# Example file paths:
# - "task_data.csv"
# - "task.json"
FILE_PATH = "task.csv"

# UI: Choose the User Interface for the system.
# Available options:
# - "console menu": For a simple console-based user interface
UI = "console menu"

# DISPLAY_DATE_FORMAT: Set the preferred display format for task due dates.
# The format must follow Python's datetime.strftime() conventions.
# Example formats:
# - "%Y-%m-%d" (2025-02-04)
# - "%d/%m/%Y" (04/02/2025)
# Note: Do not include time in the format, only date is supported.
DISPLAY_DATE_FORMAT = "%Y-%m-%d"

# Please ensure changes made here are valid to avoid runtime errors.
