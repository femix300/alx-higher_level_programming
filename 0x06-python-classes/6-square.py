#!/usr/bin/python3

"""defines a class"""


class Square:

    """a square initialization
    Args:
        size (int) : the size of the square
    """
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (
                not isinstance(value, tuple)
                or len(value) != 2
                or not all(isinstance(n, int) and n > 0 for n in value)
                ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """returns the area of the square"""
        return (self.__size * self.__size)

    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            for _ in range(self.__position[1]):
                print("")

            for _ in range(self.__size):
                if self.__position[1] == 0:
                    print(" " * self.__position[0], end='')
                print("#" * self.__size)
