#!/usr/bin/python3
"""rectangle class"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size):
        """Square initializer"""

        self.integer_validator("size", size)
        self.__size = size
        Rectangle.__init__(self, size, size)

    def __str__(self):
        """will return a nice string"""

        return "[{}] {}/{}".format("Square", self.__size, self.__size)
