class ConfigurationError(Exception):
    def __init__(self, message: str):
        super().__init__(message)


class UnsupportedFileFormatError(ConfigurationError):
    def __init__(self, message: str = "The file format is not supported by the system") -> None:
        super().__init__(message)


class InvalidUIError(ConfigurationError):
    def __init__(self, message: str = "The provided ui is invalid") -> None:
        super().__init__(message)


class InvalidDisplayDateFormatError(ConfigurationError):
    def __init__(self, message: str = "The provided display date format is invalid") -> None:
        super().__init__(message)


class FileOperationError(Exception):
    def __init__(self, message: str):
        super().__init__(message)


class FileDataError(FileOperationError):
    def __init__(self, message: str = "There is an error with the file data") -> None:
        super().__init__(message)


class CSVParsingError(FileOperationError):
    def __init__(self, message="An error occurred while parsing the CSV file") -> None:
        super().__init__(message)


class FileWriteError(FileOperationError):
    def __init__(self, message="An error occurred while writing data") -> None:
        super().__init__(message)


class TaskManagerError(Exception):
    def __init__(self, message: str):
        super().__init__(message)


class TaskNotFoundError(TaskManagerError):
    def __init__(self, message: str = "Task not found"):
        super().__init__(message)


class InvalidTaskDataError(TaskManagerError):
    def __init__(self, message: str = "Invalid task data provided"):
        super().__init__(message)


class CodeUpdateError(Exception):
    def __init__(self, message: str):
        super().__init__(message)


class UITypeMappingError(CodeUpdateError):
    def __init__(self, message: str = "The ui mapping for the given ui type is not found"):
        super().__init__(message)
