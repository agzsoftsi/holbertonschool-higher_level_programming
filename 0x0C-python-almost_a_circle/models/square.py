#!/usr/bin/python3
"""Define a Square class Task 10"""
from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """Define a Square class - Task 10."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a Square instance - Task 10."""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Print the square attributes. - Task 10"""
        return "[{}] ({}) {}/{} - {}".format(type(self).__name__, self.id,
                                             self.x, self.y, self.width)

    @property
    def size(self):
        """Getter for size."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size - based off width and height."""
        self.width = value
        self.height = value
