#!/usr/bin/python3
"""Defines a function that converts python obj to JSON"""
import json


def to_json_string(my_obj):
    """Converts a string object to JSON
        Args:
            my_obj (any): the object to convert
        Return: the JSON representation of 'my_obj'
    """
    return json.dumps(my_obj)
