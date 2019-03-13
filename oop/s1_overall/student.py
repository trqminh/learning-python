#references: https://www.python-course.eu/python3_properties.php

class Student:
    def __init__(self, name, gpa):
        self.__name = name
        self.gpa = gpa

    @property
    def gpa(self):
        return self._gpa  # must be self._gpa instead of self.gpa


    #using this setter instead of set directly (gpa is public)
    #to not break the interface, like using max function when assign
    @gpa.setter
    def gpa(self, gpa):
        self._gpa = max(0, gpa)  # must be self._gpa instead of self.gpa

    def output(self):
        print(self.__name, ": ", self.gpa)
