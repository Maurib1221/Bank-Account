from bank_account import BankAccount


# Define a subclass for a savings account that inherits from BankAccount
class SavingsAccount(BankAccount):
    def __init__(self, customer_name, current_balance, minimum_balance, interest_rate):
        # Call the parent class constructor to initialize common attributes
        super().__init__(customer_name, current_balance, minimum_balance)
        self.interest_rate = interest_rate

    #add a method to apply interest to the current balance
    def apply_interest(self):
        interest = self.current_balance * self.interest_rate / 100
        self.current_balance += interest
        print(f"Applied interest: {interest}. New balance: {self.current_balance}")

    def __str__(self):
        # Call the parent class __str__ method and add interest rate information
        return (super().__str__() +
                f"Interest Rate: {self.interest_rate}%\n")