class User:		
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    
    def make_deposit(self, amount):	
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):	
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account_balance}")
        return self

    def transfer_money(self, other_user, amount):
        # BONUS
        # let's leverage the fact that we have deposit and withdrawal methods that are available to self and other_user
        # since they're both User objects...You don't have to do it this way though
        other_user.make_deposit(amount) # could also say other_user.account_balance += amount
        self.make_withdrawal(amount) # could also say self.account_balance -= amount
        return self

blake = User("Blake Caldwell", "bcaldwell87@gmail.com")
monty = User("Monty Python", "monty@python.com")
clay = User("Clay Partridge", "clay@gmail.com")
# print(blake.name)	
# print(monty.name)	
# print(clay.name)

blake.make_deposit(100).make_deposit(200).make_deposit(50).make_withdrawal(25).display_user_balance()

monty.make_deposit(100).make_deposit(200).make_withdrawal(50).make_withdrawal(25).display_user_balance()

clay.make_deposit(100).make_withdrawal(50).make_withdrawal(50).make_withdrawal(25).display_user_balance()
