#!/usr/bin/python3
"""Module to create a rectangle, class and methods."""


class Rectangle():
    """Class to create Rectangle objects."""
    def __init__(self, width=0, height=0):
        """Initialize the width and height of rectangle."""
        self.height = height
        self.width = width

    @property
    def width(self):
        """to Get the width of rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """to Set the width."""
        if type(value) != int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """to Get the height of rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """to Set the height."""
        if type(value) != int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
