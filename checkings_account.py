from bank_account import BankAccount
class CheckingAccount(BankAccount):
    def __init__(self, customer_name, current_balance, minimum_balance, transfer_limit):
        super().__init__(customer_name, current_balance, minimum_balance)

        self.transfer_limit = transfer_limit

    # Method to transfer funds to another bank account
    def transfer(self, amount, recipient_account):
        if amount <= 0:
            print("Transfer amount must be positive.")
        elif amount > self.transfer_limit:
            print(f"Transfer failed: amount exceeds transfer limit of ${self.transfer_limit}.")
        elif self.current_balance - amount < self.minimum_balance:
            print("Transfer failed: insufficient funds after maintaining minimum balance.")
        else:
            self.current_balance -= amount
            recipient_account.current_balance += amount
            print(f"Transferred ${amount} to {recipient_account.customer_name}. New balance: {self.current_balance}")

    # Override the __str__ method to include transfer limit
    def __str__(self):
        return super().__str__() + f"Transfer Limit: ${self.transfer_limit}\n"


