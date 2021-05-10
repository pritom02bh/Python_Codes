class Person:
    def __init__(self, name, age, gender):
        self.__name = name                  # __ means private attribute
        self.__age = age
        self.__gender = gender

    @property
    def Name(self):
        return self.__name

