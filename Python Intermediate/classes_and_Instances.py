# OOP (Classes & Instances)

class Customer:
    def __init__(self, name, membership_type):  # __init__ method --> Initializer/Constractor ||  name, membership_type are Parameters (Definition) 
        self.name = name
        self.membership_type = membership_type


customers = [Customer("Pritom", "Gold"),        # Pritom, Gold are arguments (Invocation)
             Customer("Cameron", "Silver")]

print(customers[0].name)  


# Another Example -->
'''
class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last    # instance Variables
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp1 = Employee('Pritom', 'Bhowmik', 89000)
print(emp1.fullname())
print(emp1.email)
'''