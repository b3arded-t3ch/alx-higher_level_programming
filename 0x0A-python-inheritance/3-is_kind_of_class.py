#!/usr/bin/python3
"""Defines a function that checks object
    is an instance of, or if the object is an instance of a class
"""


def is_kind_of_class(obj, a_class):
    """checks if object is an instance of,
        that inherited from, the specified class

        Args:
            obj(any): the object to check
            a_class(type): the class against which to check obj

        return: True if obj belongs to a_class otherwise false
    """
    if isinstance(obj, a_class):
        return True
    return False
