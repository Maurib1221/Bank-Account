from bank_account import BankAccount


# Define a subclass for a savings account that inherits from BankAccount
class SavingsAccount(BankAccount):
    def __init__(self, customer_name, current_balance, minimum_balance, interest_rate):
        # Call the parent class constructor to initialize common attributes
        super().__init__(customer_name, current_balance, minimum_balance)
        self.interest_rate = interest_rate