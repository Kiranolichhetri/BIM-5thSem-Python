# 5. Write a Python program to create a class representing a bank. 
# Include methods for managing customer accounts and transactions.

class Bank:
    def __init__(self):
        self.accounts = {}
    
    def create_account(self, account_number, name, initial_balance=0):
        if account_number in self.accounts:
            print("Account already exists.")
        else:
            self.accounts[account_number] = {'name': name, 'balance': initial_balance}
    
    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number]['balance'] += amount
        else:
            print("Account does not exist.")
    
    def withdraw(self, account_number, amount):
        if account_number in self.accounts and self.accounts[account_number]['balance'] >= amount:
            self.accounts[account_number]['balance'] -= amount
        else:
            print("Insufficient funds or account does not exist.")
    
    def get_balance(self, account_number):
        if account_number in self.accounts:
            return self.accounts[account_number]['balance']
        else:
            print("Account does not exist.")
            return None

# Example usage:
bank = Bank()
bank.create_account(1001, 'Alice', 500)
bank.create_account(1002, 'Bob', 1000)

bank.deposit(1001, 200)
bank.withdraw(1002, 300)

print(f"Alice's balance: ${bank.get_balance(1001)}")
print(f"Bob's balance: ${bank.get_balance(1002)}")
