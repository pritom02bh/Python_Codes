'''
Class variables are defined within the class construction.
Because they are owned by the class itself, class variables are shared by all instances of the class. 
They therefore will generally have the same value for every instance unless you are using the class variable
to initialize a variable.

'''

class Employee:
    
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first                                  # those are the instance variables
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * 1.04)



emp_1 = Employee('Pritom', 'Bhowmik', 80000)
print(emp_1.fullname())

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)