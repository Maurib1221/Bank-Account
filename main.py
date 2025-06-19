from savings_account import SavingsAccount
from checkings_account import CheckingAccount

# Sample usage of SavingsAccount
savings_acc = SavingsAccount("Alice", 1500, 200, 2.5)
savings_acc.deposit(300)
savings_acc.apply_interest()
print(savings_acc)