"""
Module uses the os library to print file path to screen
"""

import os
import sys


def print_file_path():
    """
    Function prints file path to screen
    """
    if len(sys.argv) == 2:
        file = sys.argv[1]
        path = os.path.abspath(file)
        print(f"Absolute path of {file}: {path}")
    else:
        print("You have executed script with wrong number of arguments")
        print("Only specify file name to get absolute path")


if __name__ == '__main__':
    print_file_path()
