class UnsupportedFileFormat(Exception):
    def __init__(self, file_format: str):
        super().__init__(f"Unsupported file format: {file_format}")


class FileDataError(Exception):
    def __init__(self):
        super().__init__(f"There is an error with the file data")
