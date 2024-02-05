#!/usr/bin/python3
"""Defines a class list"""


class MyList(list):
    """inherits from List class"""
    def print_sorted(self):
        """print a sorted list"""
        print(sorted(self))
