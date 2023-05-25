
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
    def __init__(self,account_name,account_balance):
        self.withdrawal= []
        self.account_name=account_name
        self.account_balance=account_balance
        self.deposits= []
        self.loan_balance=0

    def show_owner(self):
        return f'{self.account_name}'
    def show_balance(self):
        return f'{self.account_balance}'
    # Add a method check_balance which returns the account’s balance
    def check_balance(self):
        return f'{self.account_balance}'
    
    # Update the deposit method to append each withdrawal transaction to the deposits list. 
    # Each transaction should be in form of a dictionary like this  
# {
#    "amount": amount,
#    "narration": “deposit”
# }

    def depositAmount(self, amount):
       self.account_balance+=amount
       depositAmount = {
                "amount": amount,
                "narration": "deposit"}
       return self.deposits.append(depositAmount)


# Update the withdrawal method to append each withdrawal transaction to the withdrawals list. 
# Each transaction should be in form of a dictionary like like this 
# {
#    "amount": amount,
#    "narration": “withdrawal”
# }
    def withdrawAmount(self, amount):
     if amount <= self.account_balance:
        self.account_balance-=amount
        withdraw= {
            "amount": amount,
            "narration": "withdraw"}
        return self.withdrawalswithdrawals.apppend(withdraw)


    


# Add a new method  print_statement which combines both deposits and withdrawals into one list and, using a for loop, prints each transaction in a new line like this
# deposit - 1000
# withdrawal - 500

        
    def print_statement(self):
        transactions = self.deposits + self.withdrawals
        for transaction in transactions:
            print(f"{transaction['narration']} - {transaction['amount']}")
        

# Add a borrow_loan method which allows a customer to borrow if they meet these conditions:
# Account has no outstanding loan
# Loan amount requested is more than 100
# Customer has made at least 10 deposits.
# Amount requested is less than or equal to 1/3 of their total sum of all deposits.
# A successful loan increases the loan_balance by requested amount

    def borrow_loan(self, loan_amount):
     if self.loan_balance == 0 and loan_amount > 100 and len(self.deposits) >= 10 and loan_amount <= self.total_deposits / 3:
      self.loan_balance += loan_amount
      return True
     else:
      return False


# Add a repay_loan method with this functionality
# A customer can repay a loan to reduce the current loan_balance
# Overpayment of a loan increases the accounts current balance


        
    def repay_loan(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.loan_balance -= amount
            print(f"Loan repayment of {amount} successful. Loan balance: {self.loan_balance}")
        else:
            overpayment = amount - self.balance
            self.loan_balance -= self.balance
            self.balance = 0
            print(f"Loan repayment of {amount} successful. Loan balance: {self.loan_balance}")
            print(f"Account balance is now 0. Overpayment: {overpayment}")
        




# Add a transfer method which accepts two attributes (amount and instance of another account). 
# If the amount is less than the current instances balance, the method transfers the requested 
# amount from the current account to the passed account. The transfer is accomplished by reducing
# the current account balance and depositing the requested amount to the passed account.
    def transferMehod(self,amount,other_account):
       if self.amount>=self.account_balance:
          self.account_balance+=amount
          other_account.append(amount)
       else:
          print("Insufficient funds.")
        
