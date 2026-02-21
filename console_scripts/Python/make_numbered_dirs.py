#! python3
# make_numbered_dirs.py - supply a directory path, starting number, and ending number
# as command line arguments to create empty directories. The directory path should contain
# the name to be created. Example arguments: C:\Folder\NewFolder 1 10

from pathlib import Path
import sys

class makeNumberedDirs:
    def __init__(self, directory, start_num, end_num):
        self.directory = directory
        self.start_num = int(start_num)
        self.end_num = int(end_num)

    def make_dirs(self) -> None:
        for number in range(self.start_num, self.end_num + 1):
            new_dir = Path(self.directory + str(number))
            new_dir.mkdir(parents=True, exist_ok=True)

def main():
    if len(sys.argv) > 1:
        class_object = makeNumberedDirs(sys.argv[1], sys.argv[2], sys.argv[3])
        class_object.make_dirs()

if __name__ == '__main__':
    main()
