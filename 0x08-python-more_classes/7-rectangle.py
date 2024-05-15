#!/usr/bin/python3
"""_summary_"""


class Rectangle:
    """_summary_"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """_summary_"""

        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def height(self):
        """_summary_
        """

        return self.__height

    @height.setter
    def height(self, value):
        """_summary_

        Args:
            value (_type_): _description_
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """_summary_
        """

        return self.__width

    @width.setter
    def width(self, value):
        """_summary_

        Args:
            value (_type_): _description_
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """Calculate and return the area of the rectangle."""

        return self.width * self.height

    def perimeter(self):
        """Calculate and return the perimeter of the rectangle."""

        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Return a string representation of the rectangle."""

        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join([str(self.print_symbol) * self.width for _ in range(self.height)])

    def __repr__(self):
        """Return a representation of the rectangle."""

        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """_summary_ """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
