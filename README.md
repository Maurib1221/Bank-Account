# Bank Account Project

This is a basic Ruby program that simulates a bank account system using object-oriented programming. It includes a base `BankAccount` class and a `CheckingAccount` subclass that adds transfer functionality.

## Features

Create accounts with a name, balance, and minimum balance.
- Deposit and withdraw funds with validation.
- Transfer money (checking only) with a set limit.
- Apply interest (savings only) using a simple interest rate.
- Enforce minimum balance rules for all accounts.

## Files
`bank_account.py`: Contains the `BankAccount` base class.
- `checking_account.py`: Defines `CheckingAccount` with `transfer()` functionality.
- `savings_account.py`: Defines `SavingsAccount` with `add_interest()` method.
- `main.py`: Runs the program by creating instances of each class and demonstrating their beha
