
class Customer:
    def __init__(self, name, membership_type):  
        self.name = name
        self.membership_type = membership_type

    def update_membership(self, new_membership):    # Added a New method to the class to update membership_type

        # We can 
        # invoke an API
        # Update a database
        # calculate Costs...........
        
        print("Calculating Cost")                       # Just to simulate something..
        self.membership_type = new_membership

    def read_customer():                                # This method is not invokable to any individual Customers.. (Static Method)
        print('Reading customer from the database')




customers = [Customer("Pritom", "Gold"),       
             Customer("Cameron", "Silver")]

print(customers[1].membership_type)
customers[1].update_membership("Gold")              # Membership Type is updated here form Silver to Gold
print(customers[1].membership_type)                 # Print the new membership_type


Customer.read_customer()                            # Using the Static Method