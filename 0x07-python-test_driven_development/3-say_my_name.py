#!/usr/bin/python3
"""
    sy_my_name
    will print a persons name
    returns nothing
"""


def say_my_name(first_name, last_name=""):
    """
        Prints a persons name
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
