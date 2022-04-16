#!python3
#
# dict_conditional.py -- function to return error messages if the input is not an even number
# 
# store conditionals or regular expressions inside of a dictionary
# loop through the dictionary and return an error message if the conditional
# is true or if the regular expression returns a match

import re
from typing import Tuple

def is_even_number(num: str) -> str:

    # store error messages in dict 
    error_messages = {
    "Error: input must be a whole number": 
        r'[^0-9]',
    "Error: input is an odd number. Please enter even number": 
        r'[13579$]',
        }

    # use list comprehension in return statement
    message = tuple(key
        for key, value
        in error_messages.items()
        if re.search(value, num)
        )
    if message == ():
        return 'Number is even'
    else:
        return message

print('Please enter an even number.')
print(is_even_number(input()))


