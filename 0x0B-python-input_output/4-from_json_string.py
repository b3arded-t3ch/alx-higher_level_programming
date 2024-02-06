#!/usr/bin/python3
"""Defines JSON-string-to-python-object function"""
import json


def from_json_string(my_str):
    """Converts a JSON sting to python object"""
    return json.loads(my_str)
