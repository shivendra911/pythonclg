class BankAccount:

    def __init__(self, balance):
        self.__balance = balance 

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, amount):
        if amount < 0:
            print("Balance cannot be negative")
        else:
            self.__balance = amount

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient amount")
        else:
            self.__balance -= amount

account = BankAccount(1000)

print(account.balance)   

account.deposit(500)
print(account.balance)

account.withdraw(200)
print(account.balance)

account.balance = -100  


print(account.__dict__)
