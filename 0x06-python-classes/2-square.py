#!/usr/bin/python3
"""A Square module with attribute type chaking"""


class Square:
    """A Square class with attribute type chaking"""

    def __init__(self, size=0):
        """Initialize a square instance"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
