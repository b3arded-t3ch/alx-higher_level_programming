#!/usr/bin/python3
"""Defines a class Student."""


class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """Initiating a new student with the attributes.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a dictionary representation of the Student."""
        if (type(attrs) is list and all(type(elm) is str for elm in attrs)):
            return {dic: getattr(self, dic)
                    for dic in attrs if hasattr(self, dic)}
        return self.__dict__

    def reload_from_json(self, json):
        """Repalaces attributes student with new values"""
        for value in json:
            setattr(self, value, json[value])
