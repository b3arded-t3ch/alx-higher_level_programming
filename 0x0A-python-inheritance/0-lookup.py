#!/usr/bin/python3
"""This represents an attribute lookup function"""


def lookup(obj):
    """This function returns the list of
        available attributes and methods of an object
    """
    return (dir(obj))
