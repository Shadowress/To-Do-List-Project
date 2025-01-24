from filehandler import FileHandler


class JSONFileHandler(FileHandler):

    def __init__(self, file_path: str):
        super().__init__(file_path)

    def load_file(self) -> None:
        pass

    def write_file(self) -> None:
        pass

    def append_file(self) -> None:
        pass
