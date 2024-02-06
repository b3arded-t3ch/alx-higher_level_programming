#!/usr/bin/python3
"""Defines a text file insertion function."""


def append_after(filename="", search_string="", new_string=""):
    """Insert text after each line containing a given string in a file.

    Args:
        filename (str): The name of the file.
        search_string (str): The string to search for within the file.
        new_string (str): The string to insert.
    """
    modified_content = ""
    with open(filename, mode='r', encoding="utf-8") as f:
        for line in f:
            modified_content += line
            if search_string in line:
                modified_content += new_string
    with open(filename, mode='w', encoding="utf-8") as n:
        n.write(modified_content)
