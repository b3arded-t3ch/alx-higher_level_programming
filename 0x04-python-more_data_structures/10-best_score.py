#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is not None:
        val_u = []
        for value in a_dictionary.values():
            val_u.append(value)
        val_u.sort()
        big_gest = val_u[-1]
        for key, value in a_dictionary.items():
            if a_dictionary[key] is None:
                return (None)
            elif a_dictionary[key] is big_gest:
                return (key)
