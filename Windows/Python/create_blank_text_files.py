#! python3
# create_blank_text_files.py
# Add blank .txt files to the specified folder. Specify the prefix using the format 'text0000'

# from pathlib import Path
import re


def main(folder: str, prefix: str, number_of_files: int) -> str:
    for i in range(number_of_files):
        regex_object = re.compile("(\D*)(\d*)").search(prefix)
        prefix_letters = regex_object.group(1)
        prefix_number_length = len(regex_object.group(2))
        open(
            folder  # folder to add files to
            + "\\"  # backslash for Windows file path
            + prefix_letters # specified prefix for blank files
            + ("0" * (prefix_number_length - len(str(i)))) # add leading zeroes to the file numbers
            + str(i) 
            + ".txt", # .txt file extension
            "x",    # creates new file if file does not exist
        )
        return "Files added to " + folder + "the name " + prefix + ".txt"


if __name__ == "__main__":
    main("C:\\test_source", "test000", 4)
