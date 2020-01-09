#!/usr/bin/python3
class Square:
    """Class Square is created"""

    def __init__(self, size=0):
        """Initializes with a size"""
        self.size = size

    @property
    def size(self):
        """method to return size value"""
        return self.__size

    @size.setter
    def size(self, value):
        """method to set a size value"""
        if type(value) != int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
            """Verify that size is not negative or 0"""
        self.__size = value

    def area(self):
        """Return the area of the square"""
        return self.__size**2

    def my_print(self):
        """Prints square with # in stdout."""
        if self.__size == 0:
            print()
        else:
            for num in range(0, self.__size):
                print('#' * self.__size)
                """loop to print the square"""
