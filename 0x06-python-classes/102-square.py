#!/usr/bin/python3
class Square:
    """
    Class that defines properties of square by: (based on 3-square.py).

    Attributes:
        size: size of a square (1 side).
    """

    def __init__(self, size=0):
        """Initializes the data."""
        self.__size = size

    def __eq__(self, other):
        """Equal."""
        if hasattr(other, 'size'):
            return self.__size == other.__size
        return self.__size == other

    def __ne__(self, other):
        """Not equal."""
        return not self.__eq__(other)

    def __lt__(self, other):
        """Less than."""
        if hasattr(other, 'size'):
            return self.__size < other.__size
        return self.__size < other

    def __le__(self, other):
        """Less than or equal."""
        if hasattr(other, 'size'):
            return self.__size <= other.__size
        return self.__size <= other

    @property
    def size(self):
        """Retrieves the size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size to a value."""
        if not isinstance(value, int) or not isinstance(value, float):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current square area."""
        return self.__size ** 2
