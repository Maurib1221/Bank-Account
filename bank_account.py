
# Define a class to represent a bank account
class BankAccount:
    # Class variable for the bank's name
    bank_title = "Sunflower Bank"

    # Initialize a new bank account with customer name, current balance, and minimum balance
    def __init__(self, customer_name, current_balance, minimum_balance):
        self.customer_name = customer_name
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance

    # Deposit a specified amount into the account
    def deposit(self, amount):
        if amount > 0:
            self.current_balance += amount
            print(f"Deposited: {amount}. New balance: {self.current_balance}")
        else:
            print("Please enter a valid amount to deposit.")

    # Withdraw a specified amount from the account if possible
    def withdraw(self, amount):
        if amount > 0 and (self.current_balance - amount) >= self.minimum_balance:
            self.current_balance -= amount
            print(f"Withdrew: {amount}. New balance: {self.current_balance}")
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    # Return a string representation of the account details
    def __str__(self):
        return (f"Bank: {self.bank_title}\n"
                f"Customer: {self.customer_name}\n"
                f"Current Balance: {self.current_balance}\n"
                f"Minimum Balance: {self.minimum_balance}\n")

# Create a bank account for Clarice and perform transactions
acc1 = BankAccount("Clarice", 1000, 100)
acc1.deposit(500)
acc1.withdraw(200)
print(acc1)

# Create a bank account for John and perform transactions
acc2 = BankAccount("John", 2000, 200)
acc2.deposit(300)
acc2.withdraw(2500)
print(acc2)


#Create two subclasses

class SavingsAccount(BankAccount):
    # Create a savings account with an interest rate
    def __init__(self, customer_name, current_balance, minimum_balance, interest_rate):
        super().__init__(customer_name, current_balance, minimum_balance)
        self.interest_rate = interest_rate

class CheckingAccount(BankAccount):
    def __init__(self, customer_name, current_balance, minimum_balance, transfer_limit):
        super().__init__(customer_name, current_balance, minimum_balance)
        self.transfer_limit = transfer_limit