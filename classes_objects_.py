# Basic example of Class and Objects

class Person:
    def __init__(self, name, age, height):      #Constructor
       self.name = name
       self.age = age
       self.height = height

    def __del__(self):                          #destructor
        print(" Object Deleted ")
 

person_1 = Person("Pritom", 25, 170)
print(person_1.name)
print(person_1.age)
print(person_1.height)


person_2 = Person("Mike", 28, 171)
print(person_2.name)
print(person_2.age)
print(person_2.height)

del person_2
