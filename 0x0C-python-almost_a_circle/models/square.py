#!/usr/bin/python3
"""
Square class module
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        init method
        """
        super().__init__(width=size, height=size, x=x, y=y, id=id)

    def __str__(self):
        """
        string representation
        """
        return "[Square] ({}) {}/{} - {}".\
            format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """
        size getter
        """
        return self.width

    @size.setter
    def size(self, width):
        """
        size setter
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.width = width

    def update(self, *args, **kwargs):
        """
        Update attributes
        """
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                setattr(self, k, v)
        elif len(args) != 0:
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                pass
        else:
            print()

    def update_csv(self, csv):
        """
        updates attributes using csv
        """
        if len(csv) != 0:
            a = 0
            b = csv.index(",")
            self.id = int(csv[a:b])
            a = b + 1
            b = csv.index(",", a)
            self.size = int(csv[a:b])
            a = b + 1
            b = csv.index(",", a)
            self.x = int(csv[a:b])
            a = b + 1
            self.y = int(csv[a])

    def to_dictionary(self):
        """
        converts to dictionary
        """
        sqr_dict = {'id': self.id, 'size': self.width, 'x': self.x}
        sqr_dict['y'] = self.y
        return sqr_dict

    def to_csv(self):
        """
        converts to csv
        """
        sqr_csv = str(self.id) + "," + str(self.size) + "," +\
            str(self.x) + "," + str(self.y)
        return sqr_csv
