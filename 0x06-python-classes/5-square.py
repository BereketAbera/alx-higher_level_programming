#!/usr/bin/python3
"""A Square module with print method"""


class Square:
    """A Square class with print method"""

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

    def my_print(self):
        """Prints hash values for size"""
        if (self.__size == 0):
            print('')
        else:
            for i in range(self.__size):
                print("#" * self.__size)
