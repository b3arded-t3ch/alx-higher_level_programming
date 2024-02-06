#!/usr/bin/python3
"""Defines a function that writes to file using JSON"""
import json


def save_to_json_file(my_obj, filename):
    """saves a python file to a JSON format"""
    with open(filename, mode="w") as f:
        return json.dump(my_obj, f)
