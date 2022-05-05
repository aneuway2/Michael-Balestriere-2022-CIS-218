"""
Micahel Balestriere
Week 13 - Final Lab!
"""


class Person:
    """main class"""

    def __init__(self, name=0, age=0):
        self.__name = name
        self.__age = age

    def set_name(self, name):
        """name"""
        self.__name = name

    def set_age(self, age):
        """age"""
        self.__age = age

    def get_name(self):
        """name"""
        return self.__name

    def get_age(self):
        """age"""
        return self.__age

    def __str__(self):
        """str"""
        return str(self.__name) + " is " + str(self.__age) + " years old!"

    def __repr__(self):
        """repr"""
        return "Name = " + str(self.__name) + ", Age = " + str(self.__age)

    def __eq__(self, other):
        """comparison"""
        if self is other:
            return True
        elif type(self) != type(other):
            return False
        else:
            return self.__age == other.__age and self.__age == other.__age

    def __lt__(self, other):
        """lt function"""
        if type(self) != type(other):
            return False
        return self.__age < other.__age

    def __ge__(self, other):
        """ge function"""
        if type(self) != type(other):
            return False
        return self.__age >= other.__age


class Student(Person):
    """subclass"""

    def __init__(self, name=0, age=0, points_earned=0, credits_taken=0):
        self.__name = name
        self.__age = age
        self.__points_earned = points_earned
        self.__credits_taken = credits_taken

    def set_name(self, name):
        """name"""
        self.__name = name

    def set_age(self, age):
        """age"""
        self.__age = age

    def set_pointsearned(self, points_earned):
        """points"""
        self.__points_earned = points_earned

    def set_creditstaken(self, credits_taken):
        """credits"""
        self.__credits_taken = credits_taken

    def get_name(self):
        """name"""
        return self.__name

    def get_age(self):
        """age"""
        return self.__age

    def get_creditstaken(self):
        """credits"""
        return self.__points_earned

    def get_pointsearned(self):
        """points"""
        return self.__points_earned

    def __calc_gpa(self):
        """gpa"""
        return self.__points_earned / self.__credits_taken

    def __str__(self):
        """str"""
        return "Name = " + str(self.__name) + ", GPA = " + str(self.__calc_gpa())

    def __repr__(self):
        """repr"""
        return (
            "Name = "
            + str(self.__name)
            + ", Age = "
            + str(self.__age)
            + ", GPA = "
            + str(self.__calc_gpa())
        )

    def __eq__(self, other):
        """comparison"""
        if self is other:
            return True
        elif type(self) != type(other):
            return False
        else:
            return (
                self.__calc_gpa == other.__calc_gpa
                and self.__calc_gpa == other.__calc_gpa
            )

    def __lt__(self, other):
        """lt function"""
        if type(self) != type(other):
            return False
        return self.__calc_gpa() <= other.__calc_gpa()

    def __ge__(self, other):
        """ge function"""
        if type(self) != type(other):
            return False
        return self.__calc_gpa() >= other.__calc_gpa()


class test_Person:
    test1 = Person("Mike", 18)
    test2 = Person("Ryan", 21)
    assert str(test1) == "Mike is 18 years old!"
    assert str(test2) == "Ryan is 21 years old!"
    assert repr(test1) == "Name = Mike, Age = 18"
    assert repr(test2) == "Name = Ryan, Age = 21"
    assert (test1 == test2) == False
    assert (test1 < test2) == True
    assert (test2 < test1) == False
    assert (test1 >= test2) == False
    assert (test2 >= test1) == True
    assert (test2 > test1) == True
    print("all checks okay1")


class test_Student:
    test3 = Student("Mike", 18, 100, 10)
    test4 = Student("Ryan", 21, 1000, 10)
    assert repr(test3) == "Name = Mike, Age = 18, GPA = 10.0"
    assert repr(test4) == "Name = Ryan, Age = 21, GPA = 100.0"
    assert str(test3) == "Name = Mike, GPA = 10.0"
    assert str(test4) == "Name = Ryan, GPA = 100.0"
    assert (test3 == test4) == False
    assert (test3 < test4) == True
    assert (test4 < test3) == False
    assert (test3 >= test4) == False
    assert (test4 >= test3) == True
    assert (test4 > test3) == True
    print("all checks okay2")
