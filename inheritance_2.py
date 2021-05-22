class Person:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def __str__(self):
        return("Name: {}, Age: {}, Height: {}".format(self.name, self.age, self.height))


class Worker(Person):
    def __init__(self, name, age, height, salary):
        super(Worker, self).__init__(name, age, height)
        self.salary = salary

    def __str__(self):
        text = super(Worker, self).__str__()

    def cal_yearly_salary(self):
        return self.salary * 12

worker1 = Worker("Roy", 23, 164, 3000)
print(worker1)
print(worker1.cal_yearly_salary())
