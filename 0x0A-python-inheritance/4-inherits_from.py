#!/usr/bin/python3
"""Defines function that confirms subclass of an object"""


def inherits_from(obj, a_class):
    """Confirms if obj is a subclass of a_class

        Args:
            obj(any): the object to check
            a_class(type): the class against which to check

        Return: True and False if otherwise
    """
    if issubclass(type(obj), a_class), and type(obj) != a_class:
        return True
    return False
