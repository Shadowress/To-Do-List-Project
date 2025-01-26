class FileDataError(Exception):
    def __init__(self):
        super().__init__(f"There is an error with the file data")
