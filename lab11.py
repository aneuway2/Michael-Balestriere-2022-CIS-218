"""
Michael Balestriere
week 11 - Test Your Classes
"""


class Shape:
    """shape class"""

    def __init__(self, width=0, length=0):
        """width and height variables"""
        self.__width = width
        self.__length = length

    def get_area(self):
        """gets area by multiplication"""
        return self.__length * self.__width

    def set_length(self, length):
        """sets the length"""
        self.__length = length

    def set_width(self, width):
        """sets the width"""
        self.__width = width

    def get_width(self):
        return self.__width

    def get_length(self):
        return self.__length

    def __str__(self):
        """returns string"""
        return (
            "The length is = "
            + str(self.__length)
            + ", The width is = "
            + str(self.__width)
            + " The area is = "
            + str(self.get_area())
        )

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


class test_Shape:
    """test class"""

    square = Shape()
    square2 = Shape(2, 2)
    assert square.get_width() == 0
    assert square.get_length() == 0
    square.set_width(5)
    square.set_length(10)
    assert square.get_width() == 5
    assert square.get_length() == 10
    # __repr__ check
    assert repr(square) == "Dimensions (5,10)"
    # __str__ check
    assert str(square) == "The length is = 10, The width is = 5 The area is = 50"
    # __eq__ check
    assert (square is square2) == False
    assert (square == square2) == False
    # __lt__ check
    assert (square < square2) == False
    assert (square2 < square) == True
    # __ge__ check
    assert (square >= square2) == True
    assert (square2 > square) == False

    print("All checks okay!")
