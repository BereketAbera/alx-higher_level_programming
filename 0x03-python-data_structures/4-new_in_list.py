#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    length = len(my_list)
    if idx < 0 or length <= idx:
        return my_list
    l_list = my_list[:]
    l_list[idx] = element
    return l_list
