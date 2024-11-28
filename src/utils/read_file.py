def read_file_as_str(path: str) -> str:
    with open(path, "r") as file:
        return file.read()
