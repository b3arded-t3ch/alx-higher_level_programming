#!/usr/bin/python3
"""Defines a function that writes to a file"""


def write_file(filename="", text=""):
    """Writes 'text' to 'filename'
        Args:
            filename (str): The name of the file to write.
            text (str): The text to write to the file.
        Returns:
            The number of characters written.
    """
    with open(filename, mode='w', encoding="utf-8") as f:
        return f.write(text)
