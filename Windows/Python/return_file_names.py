#! python3
# return_file_names.py -- create a class that returns a list of file names
# user supplies the directory and the file name prefix

from pathlib import Path


class get_file_names:
    def __init__(self, directory, prefix):
        self.directory = directory
        self.prefix = prefix

    def return_file_list(self) -> list:
        return [str(file) for file in self.directory.glob(f"{self.prefix}*")]


def main() -> None:
    class_object = get_file_names(
        Path(input("Enter a directory")), input('Enter a prefix, such as "spam"')
    )
    print(class_object.return_file_list())


if __name__ == "__main__":
    main()
