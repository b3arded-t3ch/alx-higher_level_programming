#!/usr/bin/python3
"""This class is a rebel!"""


class MyInt(Int):
    """The class rebels the standard behaviour of equality signs"""

    def __eq__(self, value):
        """turn equals to upside down"""
        return super().__eq__(value) != value

    def __ne__(self, value):
        """turn not equals to upside down"""
        return super().__ne__(value) == value
