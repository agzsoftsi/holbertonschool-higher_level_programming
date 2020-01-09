#!/usr/bin/python3
class Square:
    """Class Square is created"""

    def __init__(self, size=0):
        """Initializes with a size"""

        if type(size) != int:
            raise TypeError('size must be an integer')
            """Verify that size is not an integer"""
        if size < 0:
            raise ValueError('size must be >= 0')
            """Verify that size is not negative or 0"""
        self.__size = size
