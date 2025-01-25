from .file_handler import FileHandler


class CSVFileHandler(FileHandler):

    def load_file(self) -> None:
        ...  # todo Header for csv

    def write_file(self) -> None:
        pass

    def append_file(self) -> None:
        pass
