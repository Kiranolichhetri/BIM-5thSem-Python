# WAP to create an abstract class named Person with data members Id, name, and
# age and abstract methods getData() and display(). Derive class Employee from
# person and add member variable salary. Again derive another class customer from
# person and add member variable credit rating. Finally create objects of Employee
# and Customer and read and display their details.

from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age

    @abstractmethod
    def getData(self):
        pass

    @abstractmethod
    def display(self):
        pass

class Employee(Person):
    def __init__(self, id=None, name=None, age=None, salary=None):
        super().__init__(id, name, age)
        self.salary = salary

    def getData(self):
        self.id = input("Enter Employee ID: ")
        self.name = input("Enter Employee Name: ")
        self.age = int(input("Enter Employee Age: "))
        self.salary = float(input("Enter Employee Salary: "))

    def display(self):
        print(f"Employee Details:\nID: {self.id}\nName: {self.name}\nAge: {self.age}\nSalary: {self.salary}")

class Customer(Person):
    def __init__(self, id=None, name=None, age=None, credit_rating=None):
        super().__init__(id, name, age)
        self.credit_rating = credit_rating

    def getData(self):
        self.id = input("Enter Customer ID: ")
        self.name = input("Enter Customer Name: ")
        self.age = int(input("Enter Customer Age: "))
        self.credit_rating = float(input("Enter Customer Credit Rating: "))

    def display(self):
        print(f"Customer Details:\nID: {self.id}\nName: {self.name}\nAge: {self.age}\nCredit Rating: {self.credit_rating}")

# Create and display Employee details
employee = Employee()
employee.getData()
employee.display()

# Create and display Customer details
customer = Customer()
customer.getData()
customer.display()
