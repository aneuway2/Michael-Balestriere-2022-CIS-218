"""
Michael Balestriere
week 9 - Create an Object with a Subclass
I created a class that finds the area of
a rectangle by multiplying length and width.
The subclass tells the height of the rectangle set to a default of 10ft.
"""


class Shape(object):
    """get the area of a rectangle"""

    def __init__(self, width=10, length=10):
        print("Rectangle")
        self.length = length
        self.width = width

    def get_area(self):
        """gets area by multiplication"""
        return self.length * self.width

    def set_length(self, l_length):
        """sets the length"""
        self.length = l_length

    def set_width(self, w_width):
        """sets the width"""
        self.width = w_width

    def __str__(self):
        """returns string"""
        return (
            "The length is = "
            + str(self.length)
            + ", The width is = "
            + str(self.width)
            + " The area is = "
            + str(self.get_area())
        )


class Rectangle(Shape):
    """Height of rectangle"""

    def __init__(self, width=10, length=10, height=10):
        self.set_width(width)
        self.length = length
        self._height = height

    def __str__(self):
        return (
            "The height of your rectangle is "
            + str(self._height)
            + "Ft, The area is = "
            + str(self.get_area())
        )
