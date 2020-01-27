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

    def update(self, *args, **kwargs):
        """To update attributes in class. - Task 12"""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self._Rectangle__x = args[2]
            if len(args) >= 4:
                self._Rectangle__y = args[3]
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return dictionary representation of square - Task 14."""
        return {'id': self.id, 'size': self.size, 'x': self._Rectangle__x,
                'y': self._Rectangle__y}

    @property
    def size(self):
        """Getter for size."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size - based off width and height."""
        self.width = value
        self.height = value
