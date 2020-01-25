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
