#! python3
# regex-tester.py -- a tool for testing and viewing simple regex objects

import re

def regex_test(string):
    
    lower_regex = re.compile(r'[a-z]')
    upper_regex = re.compile(r'[A-Z]')
    num_regex = re.compile(r'\d')
    whitespace = re.compile(r'\s')
    nowhitespace = re.compile(r'\S*')
    
    lower_groups = lower_regex.findall(string)
    upper_groups = upper_regex.findall(string)
    num_groups = num_regex.findall(string)
    whitespace_groups = whitespace.findall(string)
    nowhitespace_groups = nowhitespace.findall(string)
    print('lowercse: ', lower_groups)
    print('uppercase: ', upper_groups)
    print('numbers: ', num_groups)
    print('whitespace: ', whitespace_groups)
    print('nowhitespace: ', nowhitespace_groups)

while True:
    print('This function is for testing regular expressions.\nPlease enter a value.')
    regex_test(str(input()))
