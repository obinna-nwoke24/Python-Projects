"""
Author: Obinna Jason Nwoke II
"""
import os
import sys

__main__ = "__main__"

if __main__ == "__main__":
    p = os.path.abspath('.')
    sys.path.insert(1, p)

import assets.phonebook as book
import assets.prompts as prompts

directory = book.Book()

try:
    prompts.main(directory)
except KeyboardInterrupt:
    exit()
