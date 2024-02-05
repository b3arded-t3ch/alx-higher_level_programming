#!/usr/bin/python3
"""Defines confirmation of instance of a class"""


def is_same_class(obj, a_class):
    """Is obj instance of a_class?

    Args:
        obj(any): the object to check its class.
        a_class(type): the class type against which obj is checked
    """
    if type(obj) == a_class:
        return True
    return False
