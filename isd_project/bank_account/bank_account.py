"""
Description: This module define a class representing a bank account with methods for managing balance and transactions.
Author: Vandana Bhangu

"""
from datetime import date
from patterns.observer import Subject

class BankAccount(Subject):
    LARGE_TRANSACTION_THRESHOLD: float = 9999.99
    LOW_BALANCE_LEVEL: float = 50.0

    def __init__(self, account_number: int, client_number: int, balance: float = 0.0, date_created: date = None):
        """
        Initialize a BankAccount instance.

        :param account_number: Unique identifier for the bank account.
        :param balance: Initial balance of the account (default is 0.0).
        :param client_number: Unique identifier for the client who owns the account.
        :param date_created: The date the account was created (defaults to today if None).
        """
        self.__account_number = account_number
        self.__balance = balance
        self._observers = []
        super().__init__()  # Initialize the Subject class

        # Validate account_number
        if not isinstance(account_number, int):
            raise ValueError("Account number must be an integer.")
        self.__account_number = account_number

        # Validate client_number
        if not isinstance(client_number, int):
            raise ValueError("Client number must be an integer.")
        self.__client_number = client_number
        
        # Validate if date_created is a valid date instance
        if isinstance(date_created, date):
            self._date_created = date_created
        else:
            self._date_created = date.today()

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
        """Return the current balance of the account."""
        return self.__balance

    @balance.setter
    def balance(self, amount: float):
        if amount < 0:
            raise ValueError("Balance cannot be negative.")
        self._balance = amount
    
    def subscribe(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def notify_observers(self, message):
        for observer in self._observers:
            observer.update(message)

    def deposit(self, amount: float) -> None:
        """
        Deposit a specified amount into the account.

        :param amount: The amount to deposit (must be positive).
        :raises ValueError: If the deposit amount is not positive.
        """
        if amount <= 0:
            raise ValueError(f"Deposit amount: {amount:.2f} must be positive.")
        self.update_balance(amount)

    def withdraw(self, amount: float) -> None:
        """
        Withdraw a specified amount from the account.

        :param amount: The amount to withdraw.
        :raises ValueError: If the withdrawal amount exceeds the balance.
        """
        if amount < 0:
            raise ValueError("Withdrawal amount: -75.00 must be positive.")
        if amount > self.__balance:
            raise ValueError(f"Withdrawal amount: {amount:.2f} must not exceed the account balance: {self.__balance:.2f}")
        self.update_balance(-amount)

    def __str__(self):
        """Return a string representation of the bank account."""
        return f"Account Number: {self.__account_number} Balance: ${self.__balance:.2f}\n"

    def update_balance(self, amount: float) -> None:
        """
        Update the balance of the bank account by a specified amount.

        :param amount: The amount to update the balance by (can be positive or negative).
        """
        try:
            amount = float(amount)
            previous_balance = self.__balance  # Store previous balance
            self.__balance += amount

            # Notify if the balance is below the low balance level
            if self.__balance < self.LOW_BALANCE_LEVEL:
                self.notify(f"Low balance warning ${self.__balance:.2f}: on account {self.__account_number}.")

            # Notify if the transaction amount exceeds the large transaction threshold
            if amount > self.LARGE_TRANSACTION_THRESHOLD:
                self.notify(f"Large transaction ${amount:.2f}: on account {self.__account_number}.")

        except ValueError:
            raise ValueError("Amount must be numeric.")

        
    def get_service_charges(self) -> float:
        """
        Calculates and returns the service charges for the bank account.
        :return: float - Service charge for the account.
        """
        pass
  



