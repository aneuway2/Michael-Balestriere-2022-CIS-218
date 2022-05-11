"""
Michael Balestriere
week 10 - Improved object
"""


class Shape:
    """shape class"""

    def __init__(self, width=0, length=0):
        """width and height variables"""
        self.__width = width
        self.__length = length

    def __repr__(self):
        """__repr__ function"""
        return "Dimensions (" + str(self.__width) + "," + str(self.__length) + ")"

    def __eq__(self, other):
        """comparison"""
        if self is other:
            return True
        elif type(self) != type(other):
            return False
        else:
            return self.__width == other.__width and self.__length == other.__length

    def __area(self):
        """area calculation"""
        return self.__width * self.__length

    def __lt__(self, other):
        """lt function"""
        if type(self) != type(other):
            return False
        return self.__area() < other.__area()

    def __ge__(self, other):
        """ge function"""
        if type(self) != type(other):
            return False
        return self.__area() >= other.__area()
