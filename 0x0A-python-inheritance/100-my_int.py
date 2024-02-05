#!/usr/bin/python3
"""This class is a rebel!"""


class MyInt(int):
    """The class rebels the standard behaviour of equality signs"""

    def __eq__(self, value):
        """turn equals to upside down"""
        return self.real != value

    def __ne__(self, value):
        """turn not equals to upside down"""
        return self.real == value
