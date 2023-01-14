#!/usr/bin/python3
"""
Recatngle class module
"""


from models.base import Base


class Rectangle(Base):
    """
    Class Rectangle
    """

    @property
    def width(self):
        """
        width getter
        """
        return self.__width

    @width.setter
    def width(self, width):
        """
        width setter
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width

    @property
    def height(self):
        """
        height setter
        """
        return self.__height

    @height.setter
    def height(self, height):
        """
        height setter
        """
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height

    @property
    def x(self):
        """
        x getter
        """
        return self.__x

    @x.setter
    def x(self, x):
        """
        x setter
        """
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x

    @property
    def y(self):
        """
        y getter
        """
        return self.__y

    @y.setter
    def y(self, y):
        """
        y getter
        """
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        init method
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        """
        computes area
        """
        return self.width * self.height

    def display(self):
        """
        displays rectangle with '#'
        """
        for i in range(self.y):
            print("")
        for j in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)

    def __str__(self):
        """
        string representation
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x,
                                                       self.y, self.width,
                                                       self.height)

    def update(self, *args, **kwargs):
        """
        Updates rectangle values
        """

        if len(kwargs) != 0:
            for k, v in kwargs.items():
                setattr(self, k, v)
        elif len(args) != 0:
            try:
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
                self.__x = args[3]
                self.__y = args[4]
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
            self.width = int(csv[a:b])
            a = b + 1
            b = csv.index(",", a)
            self.height = int(csv[a:b])
            a = b + 1
            b = csv.index(",", a)
            self.x = int(csv[a:b])
            a = b + 1
            self.y = int(csv[a:])

    def to_dictionary(self):
        """
        converts to dictionary
        """
        rect_dict = {'id': self.id, 'width': self.width, 'height': self.height}
        rect_dict['x'] = self.x
        rect_dict['y'] = self.y
        return rect_dict

    def to_csv(self):
        """
        converts to csv
        """
        rect_csv = str(self.id) + "," + str(self.width) + "," +\
            str(self.height) + "," + str(self.x) + "," + str(self.y)
        return rect_csv
