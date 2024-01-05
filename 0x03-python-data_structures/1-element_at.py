#!/usr/bin/python3
def element_at(my_list, idx):
    popped = my_list.pop(idx)
    if idx < 0:
        return (None)
    elif idx >= len(my_list):
        return (None)
    else:
        return (popped)
