#!/usr/bin/python3
"""Defines a function that appends to a file"""


def append_write(filename="", text=""):
    """appends a str to a file, creates the file even if it doesn't exist
        Args:
            filename (str): the file to write to
            text (str): the string to write to 'filename'
        Return: the number of characters added
    """
    with open(filename, mode='a+', encoding="utf-8") as f:
        return f.write(text)
