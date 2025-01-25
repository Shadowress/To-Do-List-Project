class UnsupportedFileFormat(Exception):
    def __init__(self, file_format: str):
        super().__init__(f"Unsupported file format: {file_format}")
