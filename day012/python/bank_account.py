#using setter and getter

class BankAccount:

    def __init__(self, balance):
        self.__balance = balance 

    def balance(self):
        return self.__balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient amount")
        else:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance
    

# account = BankAccount(1000)
# print(account.get_balance())
account = BankAccount(1000)
# print(account.balance)   # NOT a function call

# BankAccount.balance.__get__(account, BankAccount)

