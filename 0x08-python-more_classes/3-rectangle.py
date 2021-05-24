#!/usr/bin/python3
"""Create a rectangle class"""


class Rectangle:
    """Rectangle class"""

    def __init__(self, width=0, height=0):
        """instantiate instance reactangle"""

        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """width getter"""

        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""

        if type(value) is not int:
                raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """height getter"""

        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """calculate rectangle area"""

        return self.height * self.width

    def perimeter(self):
        """calculate rectangle perimeter"""

        if self.height * self.width == 0:
            return 0

        return (self.height * 2 + self.width * 2)

    def __str__(self):
        """return user friendly string"""

        rct_str = ''
        if self.height == 0 or self.width == 0:
            return rct_str
        for j in range(self.height):
            for i in range(self.width):
                rct_str += '#'
            if j != self.height - 1:
                rct_str += '\n'
        return rct_str
