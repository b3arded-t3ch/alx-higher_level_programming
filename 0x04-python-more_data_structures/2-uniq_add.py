#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_list = []
    uniq_sum = 0
    for i in my_list:
        if i not in uniq_list:
            uniq_list.append(i)
    for uniq in uniq_list:
        uniq_sum += uniq
    return (uniq_sum)
