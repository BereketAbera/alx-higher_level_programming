#!/usr/bin/python3
class Square:
    """A Square class with position attribute"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a square instance"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
        if type(position) is not tuple or len(position) != 2 or \
                type(position[0]) is not int or type(position[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    def area(self):
        """Calculates the area of the square"""
        return self.__size ** 2

    @property
    def size(self):
        """Size property getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """Size property setter"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Position property getter"""
        return self.__position

    @position.setter
    def position(self, value):
        """Position property setter"""
        if type(value) is not tuple or len(value) != 2 or type(value[0]) \
                is not int or type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def my_print(self):
        """Prints hash values for size and position"""
        if (self.__size == 0):
            print('')
        else:
            for i in range(self.__size):
                print(" " * self.__position[0], end='')
                print("#" * self.__size)
