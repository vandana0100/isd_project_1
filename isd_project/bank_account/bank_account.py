"""
Description: This module define a class representing a bank account with methods for managing balance and transactions.
Author: Vandana Bhangu

"""

class BankAccount:
    def __init__(self, account_number: int, client_number: int, balance: float):
        # Validate account_number
        if not isinstance(account_number, int):
            raise ValueError("Account number must be an integer.")
        self.__account_number = account_number
        
        # Validate client_number
        if not isinstance(client_number, int):
            raise ValueError("Client number must be an integer.")
        self.__client_number = client_number
        
        # Validate balance
        try:
            self.__balance = float(balance)
        except ValueError:
            self.__balance = 0.0

    @property
    def account_number(self) -> int:
        return self.__account_number

    @property
    def client_number(self) -> int:
        return self.__client_number

    @property
    def balance(self) -> float:
        return self.__balance

    def update_balance(self, amount: float) -> None:
        try:
            amount = float(amount)
            self.__balance += amount
        except ValueError:
            raise ValueError("Amount must be numeric.")

    def deposit(self, amount: float) -> None:
        if not isinstance(amount, (int, float)):
            raise ValueError(f"Deposit amount: {amount} must be numeric.")
        if amount <= 0:
            raise ValueError(f"Deposit amount: {amount:.2f} must be positive.")
        self.update_balance(amount)

    def withdraw(self, amount: float) -> None:
        if not isinstance(amount, (int, float)):
            raise ValueError(f"Withdraw amount: {amount} must be numeric.")
        if amount <= 0:
            raise ValueError(f"Withdrawal amount: {amount:.2f} must be positive.")
        if amount > self.__balance:
            raise ValueError(f"Withdrawal amount: {amount:.2f} must not exceed the account balance: {self.__balance:.2f}")
        self.update_balance(-amount)

    def __str__(self) -> str:
        return f"Account Number: {self.__account_number} Balance: ${self.__balance:,.2f}\n"
