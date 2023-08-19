"""
Module reads and writes files
"""

import sys


def read():
    """
    function reads text file and extracts my firstname and lastname
    """
    if len(sys.argv) == 2:
        file = sys.argv[1]
        try:
            with open(file, 'r') as file:
                file_ = file.read()
                names = []
                names = file_.split(" ")
                print(f"First name: {names[1]}")
                print(f"Middle name: {names[-1]}")
                print(f"Surname: {names[0]}")
        except FileNotFoundError:
            print('File Not Found')
            print('Please check for spelling errors and confirm that file path is correct')
    else:
        print('You executed script with wrong number of arguments')


if __name__ == '__main__':
    read()
