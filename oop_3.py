# __str__ ,  __eq__

class Customer:
    def __init__(self, name, membership_type):  
        self.name = name
        self.membership_type = membership_type

    def update_membership(self, new_membership):    

        print("Calculating Cost") 
        self.membership_type = new_membership
    
    def __str__(self):                                    # __str__  givers actual data, not the memory adderess
         return self.name + ' ' + self.membership_type    # returns the name and membership_type || Without it, it give us the memory address.

    def print_all_customers(customers):                   # for printing all the customers  || No need the self
        for customer in customers:
            print(customer)

    def __eq__(self, other):                                # comparing two customers
        if self.name == other.name and self.membership_type == other.membership_type:
            return True
        
        return False

         

customers = [Customer("Pritom", "Gold"),       
             Customer("Cameron", "Silver")]

print(customers[1])                                       # it prints the name and membership_type || Without it, it give us the memory address.


print(" \n ")

Customer.print_all_customers(customers)                   # It will print all the customers

print(customers[0] == customers[1])                       # checking whether this two customers are same or not...