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

# Sample usage of CheckingAccount
checking_acc = CheckingAccount("Charles", 1200, 100, 500)
recipient = BankAccount("Jordan", 400, 100)

checking_acc.transfer(300, recipient)  # valid transfer
print(checking_acc)
print(recipient)
# Second sample usage of CheckingAccount
checking_acc2 = CheckingAccount("Alex", 800, 200, 250)
recipient2 = BankAccount("Taylor", 500, 50)

checking_acc2.transfer(400, recipient2)  # exceeds transfer limit
checking_acc2.transfer(200, recipient2)  # valid transfer
print(checking_acc2)
print(recipient2)