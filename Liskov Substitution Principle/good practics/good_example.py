from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self, balance=0):
        self.balance = balance

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    def get_balance(self):
        return self.balance


class SavingsAccount(BankAccount):
    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount


class CurrentAccount(BankAccount):
    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount


def make_payment(account: BankAccount, amount):
    account.withdraw(amount)
    print(f"Remaining Balance: {account.get_balance()}")


savings = SavingsAccount(1000)
current = CurrentAccount(2000)

make_payment(savings, 500)
make_payment(current, 500)