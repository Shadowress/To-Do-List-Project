class UnsupportedFileFormatError(Exception):
    def __init__(self, message: str = "The file format is not supported by the system") -> None:
        super().__init__(message)


class FileDataError(Exception):
    def __init__(self, message: str = "There is an error with the file data") -> None:
        super().__init__(message)


class CSVParsingError(Exception):
    def __init__(self, message="An error occurred while parsing the CSV file") -> None:
        super().__init__(message)
