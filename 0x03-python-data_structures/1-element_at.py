#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0 or idx >= len(my_list):
        return (None)
    else:
        popped_element = my_list.pop(idx)
    return (popped_element)
