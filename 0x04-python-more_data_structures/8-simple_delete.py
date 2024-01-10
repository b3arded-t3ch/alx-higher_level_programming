#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if a_dictionary is not None:
        for i in list(a_dictionary.keys()):
            if i == key:
                del a_dictionary[key]
        return (a_dictionary)
