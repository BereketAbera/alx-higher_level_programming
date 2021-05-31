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
