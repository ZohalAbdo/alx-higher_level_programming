#!/usr/bin/python3
"""_summary_ """


class Square:
    """_summary_"""

    def __init__(self, size=0):
        """

        Args:
            size (_type_): _description_
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """_summary_"""

        return (self.__size * self.__size)

    @property
    def size(self):
        """

        Returns:
            _type_: _description_
        """

        return self.__size

    @size.setter
    def size(self, value):
        """_summary_

        Args:
            value (_type_): _description_

        Raises:
            TypeError: _description_
            ValueError: _description_
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """_summary_"""

        if self.__size == 0:
            print()
        for i in range(self.__size):
            for j in range(self.__size):
                print("#")
            print()
