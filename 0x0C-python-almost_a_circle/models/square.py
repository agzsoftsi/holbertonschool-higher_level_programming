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
        return ('[Square] (' + str(self.id) + ') ' + str(self._Rectangle__x) +
                '/' + str(self._Rectangle__y) + ' - ' +
                str(self._Rectangle__width))
