# Python program that implements the Account and SavingAccount classes with the specified requirements, 
# including methods for depositing, withdrawing, transferring funds, displaying data, and verifying operations:


class Account:
    def __init__(self, acc_number, acc_name, balance):
        self.acc_number = acc_number
        self.acc_name = acc_name
        self.balance = balance

    def display(self):
        print(f"Account Number: {self.acc_number}")
        print(f"Account Name: {self.acc_name}")
        print(f"Balance: {self.balance}")

class SavingAccount(Account):
    minimum_balance = 1000  # Class variable for minimum balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if SavingAccount.verify(amount):
            if self.balance - amount >= SavingAccount.minimum_balance:
                self.balance -= amount
                print(f"Withdrawn {amount}. New balance: {self.balance}")
            else:
                print("Insufficient balance to withdraw.")
        else:
            print("Invalid amount for withdrawal.")

    def transfer(self, amount, recipient):
        if SavingAccount.verify(amount):
            if self.balance - amount >= SavingAccount.minimum_balance:
                self.balance -= amount
                recipient.balance += amount
                print(f"Transferred {amount} to {recipient.acc_name}. New balance: {self.balance}")
            else:
                print("Insufficient balance to transfer.")
        else:
            print("Invalid amount for transfer.")

    @classmethod
    def displayMinBalance(cls):
        print(f"Minimum Balance for Saving Account: {cls.minimum_balance}")

    @staticmethod
    def verify(amount):
        if amount > 0:
            return True
        else:
            return False

# Demonstration of operations
sa1 = SavingAccount("SA001", "John Doe", 5000)
sa2 = SavingAccount("SA002", "Jane Smith", 3000)

sa1.display()
print("")

sa1.deposit(2000)
print("")

sa1.withdraw(1500)
print("")

sa1.transfer(1000, sa2)
print("")

SavingAccount.displayMinBalance()
