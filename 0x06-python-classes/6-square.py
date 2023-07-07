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
            [print("") for i in range(0, self.__position[1])]
            for i in range(0, self.__size):
                [print(" ", end="") for j in range(0, self.__position[0])]
                [print("#", end="") for k in range(0, self.__size)]
                print("")
