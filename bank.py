
# 2) Create 3 files in the classes directory car.py, fruit.py, and bank.py.
#  Define the following classes in each module respectively. 
# Car
# Fruit
# Account
# Each class should have one class attribute and three instance variables.

# Discuss in your group and come up with the attributes and 
# three methods (behaviours) for each class and implement them



class Account():
    bank="Equity"
    def __init__(self,withdraw,account_name,account_balance):
        self.withdraw=withdraw
        self.account_name=account_name
        self.account_balance=account_balance
    def show_owner(self):
        return f'{self.account_name}'
    def show_balance(self):
        return f'{self.account_balance}'
    def withdraw_money(self):
        return  {self.account_balance} - {self.withdraw}


