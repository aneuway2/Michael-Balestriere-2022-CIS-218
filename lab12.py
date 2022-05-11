"""
Michael Balestriere
week 12 - objects in python continued
"""

import sqlite3


class GradeBook:
    """class"""
    def __init__(self):
        """Gradebook class"""
        connection = sqlite3.connect(":memory:")
        self.__database = connection.cursor()
        self.__database.execute("CREATE TABLE gradebook(student, grade)")
        print("table created")

    def upload_grades(self):
        """upload grades"""
        grade_list = [
            ("Michael", 100),
            ("Ryan", 98),
            ("Dylan", 86),
            ("Alyssa", 100),
            ("Gina", 81),
        ]
        self.__database.executemany("INSERT INTO gradebook VALUES(?,?)", grade_list)
        self.__database.connection.commit()
        return "gradebook completed"

    def student_grades(self):
        """get student grade"""
        self.__database.execute("SELECT grade FROM gradebook WHERE student = 'Michael'")
        return self.__database.fetchall()
        return "DONE"
        self.__database.connection.close()


def test_gradebook():
    """ test method does not work properly, unsure how to complete.
        This is what I came up with instead. Only checks if gradebook class works.
        How do I change the name to be tested? """
    test = GradeBook()
    assert test.upload_grades()
    assert test.student_grades()
    assert test.student_grades() == [(100,)]
    print("all checks okay!")


test_gradebook()
