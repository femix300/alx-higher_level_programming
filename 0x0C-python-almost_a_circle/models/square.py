#!/usr/bin/python3
"""A module containing the square class"""

from models.rectangle import Rectangle


class Square(Rectangle):

    """A square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a new square"""
        super().__init__(size, size, x, y, id)

    def update(self, *args, **kwargs):
        """updates the square class"""
        if args:
            try:
                self.id = args[0]
                self.width = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                pass
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.width = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """A string representation of the square"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
