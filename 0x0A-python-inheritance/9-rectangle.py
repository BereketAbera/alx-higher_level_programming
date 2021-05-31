#!/usr/bin/python3
"""rectangle class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """rectangle class"""

    def __init__(self, width, height):
        """rectangle initializer"""

        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """implement area"""

        return self.__width * self.__height

    def __str__(self):
        """will return a nice string"""

        return "[{}] {}/{}".format("Rectangle", self.__width, self.__height)
