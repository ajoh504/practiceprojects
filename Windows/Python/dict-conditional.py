#!python3
# dict_conditional.py -- UNFINISHED

# create function to return error messages if the input is not an even number

import re

def is_even_number(num: str) -> str:

    # store error messages in dict 
    error_messages = {
    0: "Error: input must be a whole number",
    1: "Error: input must be a whole number",
    2: "Error: input is an odd number. Please enter even number",
        }

    # store conditionals in dict 
    # match error_conditionals keys w/ error_messages keys
    error_conditionals = {
    0: True if not r'(\d+)(\.)(\d+)' else False,
    1: True if r'[\.\^\$\*\+\?\{\}\[\]\\\|\(\)]' else False,
    2: True if int(num) % 2 == 1 else False
        }

    # use list comprehension in return statement
    return [error_messages[key]
                for key, value
                in error_conditionals.items()
                if value]

print('Please enter an even number.')
print(is_even_number(input()))

