#!python3
# user_input_cd.py -- Prompt user to change directories
#
# create main function to check for valid filepath 
# change directories if path is valid

import os
from pathlib import Path

def main(user_input: str) -> str:
    
    new_path = Path(user_input)
    if new_path.is_file() == True:
        return 'Error: cannot CD to a file!'
    elif new_path.exists() != True:
        return 'Error: directory does not exist!'
    else:
        os.chdir(new_path)
        return 'Directory changed to ' + str(new_path)

if __name__ == "__main__":
    # create print statements
    print('Use this script to change directories.\nPlease enter a valid Windows file path.')
    print(main(input()))
