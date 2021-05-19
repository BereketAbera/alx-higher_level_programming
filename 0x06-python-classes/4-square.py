#!/usr/bin/python3
"""A Square module with setter and getters"""


class Square:
    """A Square class with setter and getters"""

    def __init__(self, size=0):
        """Initialize a square instance"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Calculates the area of the square"""
        return self.__size ** 2

    @property
    def size(self):
        """Size property getter"""
        return self.__size

    @size.setter
    def size(self, size):
        """Size property setter"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
