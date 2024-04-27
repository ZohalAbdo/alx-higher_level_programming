#!/usr/bin/python3
"""_summary_"""


class Rectangle:
    """_summary_"""

    def __init__(self, width=0, height=0):
        """_summary_"""

        self.__width = width
        self.__height = height

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

        try:
            self.__width = value
        except Exception as e:
            print("[{}] {}".format(e.__class__.__name___, e))
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

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

        try:
            self.__height = value
        except Exception as e:
            print("[{}] {}".format(e.__class__.__name___, e))
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
