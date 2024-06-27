#  Python program that defines the classes as described and 
#  demonstrates creating an object of the 'EmpCustomer' class, reading, and displaying its details:

class Customer:
    def __init__(self, cid, cname, address):
        self.cid = cid
        self.cname = cname
        self.address = address

    def display(self):
        print(f"Customer ID: {self.cid}")
        print(f"Customer Name: {self.cname}")
        print(f"Customer Address: {self.address}")

class Employee:
    def __init__(self, eid, ename, post):
        self.eid = eid
        self.ename = ename
        self.post = post

    def display(self):
        print(f"Employee ID: {self.eid}")
        print(f"Employee Name: {self.ename}")
        print(f"Employee Post: {self.post}")

class EmpCustomer(Customer, Employee):
    def __init__(self, cid, cname, address, eid, ename, post, rating):
        Customer.__init__(self, cid, cname, address)
        Employee.__init__(self, eid, ename, post)
        self.rating = rating

    def display(self):
        super().display()
        super(Employee, self).display()
        print(f"Customer Rating: {self.rating}")

# Create and display EmpCustomer details
emp_customer = EmpCustomer("C123", "John Doe", "123 Main St", "E456", "Jane Smith", "Manager", 4.5)
emp_customer.display()
