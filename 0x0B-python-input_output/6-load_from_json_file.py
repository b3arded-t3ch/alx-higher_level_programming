#!/usr/bin/python3
"""Defines function that creates obj from JSON file"""
import json


def load_from_json_file(filename):
    """creates a python object from json file"""
    with open(filename) as f:
        return json.load(f)
