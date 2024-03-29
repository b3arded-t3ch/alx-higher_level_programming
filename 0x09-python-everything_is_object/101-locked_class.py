#!/usr/bin/python3
"""Defines a locked class."""


class LockedClass:
    """
    The user can't instantiate new LockedClass attributes
    except attributes called 'first_name'.
    """

    __slots__ = ["first_name"]
