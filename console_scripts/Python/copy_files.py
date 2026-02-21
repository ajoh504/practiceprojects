# These functions receive two arguments: a list of file paths and a destination Windows drive, such as "D:/"
# If the directory does not exist on the destination drive, it is created, and the file paths or directory
# trees are copied. 
# WARNING: Matching file names on the destination drive will be completely overwritten. 

import os
import shutil
from pathlib import Path

def copy_files(file_list: list, destination: str) -> None:
    for file_path in file_list:
        if Path(destination + '/'.join(Path(file_path).parts[1:-1])).exists() == False:
            os.makedirs(destination + '/'.join(Path(file_path).parts[1:-1]))
        shutil.copy(file_path, destination + '/'.join(Path(file_path).parts[1:-1]))

def copy_dirs(dir_list: list, destination: str):
    for dir_path in dir_list:
        if Path(destination + '/'.join(Path(dir_path).parts[1:])).exists() == False:
            os.makedirs(destination + '/'.join(Path(dir_path).parts[1:]))
        shutil.copytree(dir_path, destination + '/'.join(Path(dir_path).parts[1:]), dirs_exist_ok=True)
