#!/usr/bin/python3
"""Define a square with position coordinates."""


class Square:
    """Class Square is created."""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes with a size"""
        self.size = size
        self.position = position

    def __eq__(self, other):
        """Standard operators as functions two squares are equal."""
        return self.__size == other.__size

    def __ne__(self, other):
        """Standard operators as functions two squares are not equal."""
        return self.__size != other.__size

    def __lt__(self, other):
        """Standard operators as functions square 1 is less than square 2."""
        return self.__size < other.__size

    def __le__(self, other):
        """Standard operators as functions square 1 is less than or equal to square 2."""
        return self.__size <= other.__size

    def __gt__(self, other):
        """Standard operators as functions square 1 is greater than square 2."""
        return self.__size > other.__size

    def __ge__(self, other):
        """Standard operators as functions square 1 is greater than or equal to square 2."""
        return self.__size >= other.__size

    @property
    def size(self):
        """method to return size value."""
        return self.__size

    @size.setter
    def size(self, value):
        """method to set a size value."""
        if type(value) != int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
            """Verify that size is not negative or 0"""
        self.__size = value

    def area(self):
        """Return the area of the square"""
        return self.__size**2

