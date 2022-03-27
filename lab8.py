"""
Michael Balestriere
week 8 - create a python class
I am trying to create a class that finds the area of
a rectangle by multiplying length and width
"""


class Measure:
    """get the area of a rectangle"""

    def __init__(self):
        print("Rectangle")
        self.__length = 10
        self.__width = 10

    def get_area(self):
        """gets area by multiplication"""
        return self.__length * self.__width

    def set_length(self, l_length):
        """sets the length"""
        self.__length = l_length

    def set_width(self, w_width):
        """sets the width"""
        self.__width = w_width
