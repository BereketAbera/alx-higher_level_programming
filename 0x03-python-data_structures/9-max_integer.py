#!/usr/bin/python3
def max_integer(my_list=[]):
    max = None
    for index, value in enumerate(my_list):
        if index == 0:
            max = value
        else:
            max = max if max > value else value
    return max
