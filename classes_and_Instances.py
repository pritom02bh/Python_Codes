# OOP (Classes & Instances)

class Employee:
    
    def __init__(self, first, last, pay):

emp_1 = Employee()
emp_2 = Employee()

print(emp_1)
print(emp_2)

emp_1.first = 'Pritom' 
emp_1.last = 'Bhowmik'
emp_1.email = 'pritom01bh@gmail.com'
emp_1.pay = 70000

emp_2.first = 'Jastin' 
emp_2.last = 'Corea'
emp_2.email = 'js21c@gmail.com'
emp_2.pay = 67000

print(emp_1.email)
print(emp_2.email)





