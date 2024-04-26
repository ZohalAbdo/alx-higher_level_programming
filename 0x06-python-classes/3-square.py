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

            return(self.__size * self.__size)
