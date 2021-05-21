class Person:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def __str__(self):
        return("Name: {}, Age: {}, Height: {}".format(self.name, self.age, self.height))


class Worker:
    def __init__(self, name, age, height, salary):
        