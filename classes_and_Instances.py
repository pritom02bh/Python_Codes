# OOP (Classes & Instances)

class Customer:
    def __init__(self, name, membership_type):  # __init__ method --> Initializer/Constractor ||  name, membership_type are Parameters (Definition) 
        self.name = name
        self.membership_type = membership_type


customers = [Customer("Pritom", "Gold"),        # Pritom, Gold are arguments (Invocation)
             Customer("Cameron", "Silver")]

print(customers[0].name)  