#! python3
# return_file_names.py -- create a class that returns a list of file names
# user supplies the directory and the file name prefix

from pathlib import Path


class get_file_names:
    def __init__(self, directory, prefix):
        self.directory = directory
        self.prefix = prefix

    def return_file_list(self) -> list:
        return_list = []
        for file in self.directory.glob(f"{self.prefix}*"):
            return_list.append(str(file))
        return return_list


def main() -> None:
    class_object = get_file_names(
        Path(input("Enter a directory")), input('Enter a prefix, such as "spam"')
    )
    class_object.return_file_list()


if __name__ == "__main__":
    main()
