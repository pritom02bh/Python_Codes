class Person:
    def __init__(self, name, age, gender):
        self.__name = name                  # __ means private attribute
        self.__age = age
        self.__gender = gender

    @property                               # A property is created to access the private attribute.
    def Name(self):
        return self.__name                  # We can use it later to access the attribute.
    
    @property
    def Age(self):
        return self.__age


    @Name.setter                            # setter
    def Name(self, value):
        self.__name = value

    @Age.setter    
    def Age(self, value):
        self.__age = value

    @staticmethod                           # A Static Method
    def mymethod():
        print("This is a static method")
    


Person.mymethod()


p1 = Person("Pritom", 20, 'M')
print(p1.Name)
print(p1.Age)


