#!/usr/bin/python3
"""A function that reads a file"""


def read_file(filename=""):
    """This function reads a text file and prints it to stdout"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
