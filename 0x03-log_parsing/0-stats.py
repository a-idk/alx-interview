#!/usr/bin/python3
"""
Title: a script that reads stdin line by line and computes metrics:
Description:
Author: @a_idk
"""


import sys


# creating the status code dictionary
code_dict = {
            '200': 0,
            '301': 0,
            '400': 0,
            '401': 0,
            '403': 0,
            '404': 0,
            '405': 0,
            '500': 0
            }

size = 0  # total size
count = 0  # keep count of the number lines counted

try:
    for line in sys.stdin:
        line_args = line.split(" ")

        if len(line_args) > 4:
            status_code = line_args[-2]
            file_size = int(line_args[-1])

            # if the status code exists in the code dictionary
            if status_code in code_dict.keys():
                code_dict[status_code] = code_dict[status_code] + 1

            # updating the size
            size = size + file_size

            # updating the count
            count = count + 1

        if count == 10:
            count = 0
            print('File size: {}'.format(size))

            # display status code
            for key, value in sorted(code_dict.items()):
                if value != 0:
                    print('{}: {}'.format(key, value))

# Handling exceptions
except Exception as err:
    pass

finally:
    print('File size: {}'.format(size))
    for key, value in sorted(code_dict.items()):
        if value != 0:
            print('{}: {}'.format(key, value))
