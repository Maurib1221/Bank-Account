from savings_account import SavingsAccount
from checkings_account import CheckingAccount

# Sample usage of SavingsAccount
savings_acc = SavingsAccount("Alice", 1500, 200, 2.5)
savings_acc.deposit(300)
savings_acc.apply_interest()
print(savings_acc)
#Second sample usage of SavingsAccount
savings_acc2 = SavingsAccount("Bob", 1000, 100, 3.0)
savings_acc2.withdraw(200)
savings_acc2.apply_interest()
print(savings_acc2)
