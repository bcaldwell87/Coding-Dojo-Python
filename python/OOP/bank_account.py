class BankAccount:
    def __init__(self, int_rate = 0, balance = 0):
            self.int_rate = int_rate
            self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self

    def yield_interest(self):
        self.balance *= 1.25
        return self

blake = BankAccount(balance=1000)
clay = BankAccount(balance=500)

blake.deposit(100).deposit(200).deposit(50).withdraw(25).yield_interest().display_account_info()
clay.deposit(1000).deposit(2000).withdraw(500).withdraw(1001).yield_interest().display_account_info()