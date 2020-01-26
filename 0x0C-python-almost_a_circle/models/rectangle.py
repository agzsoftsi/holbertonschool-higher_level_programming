#!/usr/bin/python3
"""Define a Rectangle class."""

from models.base import Base


class Rectangle(Base):
    """Define a Rectangle class. - Task 2"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a Rectangle instance. - Task 2"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def area(self):
        """Return the area of the rectangle - Task4."""
        return self.__width * self.__height

    def display(self):
        """Return a picture of the object. - Task5"""
        print('\n' * self.__y + (' ' * self.__x + '#' * self.__width + '\n') *
              self.__height, end='')

    def __str__(self):
        """Print the rectangle. - Task 6"""
        return "[{}] ({}) {}/{} - {}/{}".format(type(self).__name__, self.id,
                                                self.x, self.y, self.width,
                                                self.height)

    def update(self, *args, **kwargs):
        """Update the rectangle: id, width, height, x, y - Task 8 - Task 9."""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.__width = args[1]
            if len(args) >= 3:
                self.__height = args[2]
            if len(args) >= 4:
                self.__x = args[3]
            if len(args) >= 5:
                self.__y = args[4]
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    @property
    def width(self):
        """Getter for width. - Task 3"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width. - Task 3"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError('width must be > 0')
        else:
            self.__width = value

    @property
    def height(self):
        """Getter for height. - Task 3"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height. - Task 3"""
        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif value <= 0:
            raise ValueError('height must be > 0')
        else:
            self.__height = value

    @property
    def x(self):
        """Getter for x - Task3."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x - Task3."""
        if type(value) is not int:
            raise TypeError('x must be an integer')
        elif value < 0:
            raise ValueError('x must be >= 0')
        else:
            self.__x = value

    @property
    def y(self):
        """Getter for y - Task3."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y - Task3."""
        if type(value) is not int:
            raise TypeError('y must be an integer')
        elif value < 0:
            raise ValueError('y must be >= 0')
        else:
            self.__y = value
