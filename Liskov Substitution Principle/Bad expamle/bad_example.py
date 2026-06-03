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


class SavingsAccount(BankAccount):
    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient balance")
        self.balance -= amount


class CheckingAccount(BankAccount):
    def __init__(self, balance=0, overdraft_limit=0):
        super().__init__(balance)
        self.overdraft_limit = overdraft_limit

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance - amount < -self.overdraft_limit:
            raise ValueError("Overdraft limit exceeded")
        self.balance -= amount