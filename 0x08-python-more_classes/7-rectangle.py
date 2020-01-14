#!/usr/bin/python3
"""Module to create a rectangle, class and methods."""


class Rectangle():
    """Class to create Rectangle objects."""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initialize the width and height of rectangle."""
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    def __str__(self):
        """To Print the rectangle."""
        string = ''
        if self.__height == 0 or self.__width == 0:
            return string
        string = string + ((str(self.print_symbol) * self.__width + '\n') *
                           self.__height)
        return string[:-1]

    def __repr__(self):
        """To return a String of Rectangle Representation."""
        return "{}({}, {})".format(type(self).__name__,
                                   self.width, self.height)

    def __del__(self):
        """To Delete Rectangle."""
        print('Bye rectangle...')
        Rectangle.number_of_instances -= 1

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

    def area(self):
        """To Return the rectangle area."""
        return self.__width * self.__height

    def perimeter(self):
        """To Return the rectangle perimeter."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2
