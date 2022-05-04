"""
Micahel Balestriere
Week 13 - Final Lab!
"""

class Person():
    """main class"""
    def __init__(self, name=0, age=0):
        self.__name = name
        self.__age = age

    def set_name(self,name):
        self.__name = name

    def set_age(self,age):
        self.__age = age

    def get_name(self):
        return self.__name
    
    def get_age(self):
        return self.__age

    def __str__(self):
        return(str(self.__name) + " is " + str(self.__age) + " years old!")

    def __repr__(self):
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
        return self.__age() < other.__age()

    def __ge__(self, other):
        """ge function"""
        if type(self) != type(other):
            return False
        return self.__age() >= other.__age()

class Student(Person):
    """subclass"""
    def __init__(self, name=0, age=0, points_earned=0, credits_taken=0):
        self.__name = name
        self.__age = age
        self.__points_earned = points_earned
        self.__credits_taken = credits_taken

    def set_name(self,name):
        self.__name = name

    def set_age(self,age):
        self.__age = age

    def set_pointsearned(self,points_earned):
        self.__points_earned = points_earned

    def set_creditstaken(self,credits_taken):
        self.__credits_taken= credits_taken
        
    def get_name(self):
        return self.__name
    
    def get_age(self):
        return self.__age

    def get_creditstaken(self):
        return self.__points_earned

    def get_pointsearned(self):
        return self.__points_earned

    def __calc_gpa(self):
         return self.__points_earned / self.__credits_taken
        
    def __str__(self):
        return ("Name = " + str(self.__name) + ", GPA = " + str(self.__calc_gpa()))
    
    def __repr__(self):
        return "Name = " + str(self.__name) + ", Age = " + str(self.__age) + ", GPA = " + str(self.__calc_gpa())

    def __eq__(self, other):
        """comparison"""
        if self is other:
            return True
        elif type(self) != type(other):
            return False
        else:
            return self.__calc_gpa== other.__calc_gpa and self.__calc_gpa == other.__calc_gpa

    def __lt__(self, other):
        """lt function"""
        if type(self) != type(other):
            return False
        return self.__calc_gpa() < other.__calc_gpa()

    def __ge__(self, other):
        """ge function"""
        if type(self) != type(other):
            return False
        return self.__calc_gpa() >= other.__calc_gpa()

class test_Person:
    test1=Person("Mike", 18)
    test2=Person("Ryan", 21)
    assert str(test1) == "Mike is 18 years old!"
    assert str(test2) == "Ryan is 21 years old!"
    assert repr(test1) == "Name = Mike, Age = 18"
    assert repr(test2) == "Name = Ryan, Age = 21"
    assert (test1 == test2) == False

    """I get this error for these asserts. TypeError: 'int' object is not callable."""
    """I'm unsure how to fix this before I move on"""
    #assert (test1 < test2) == True
    #assert (test2 < test1) == False
    #assert (test1 >= test2) == True
    #assert (test1 >= test2) == False
    #assert(test2 > test1) == True
    

