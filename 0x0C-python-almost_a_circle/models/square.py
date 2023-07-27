#!/usr/bin/python3
"""A module containing the square class"""

from models.rectangle import Rectangle


class Square(Rectangle):

    """A square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a new square"""
        super().__init__(size, size, x, y, id)

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
