"""
Description: Unit tests for the ChequingAccount class, which inherits from BankAccount.
Author: Vandana Bhangu

"""
from datetime import date
import datetime
from bank_account.bank_account import BankAccount
from patterns.strategy.overdraft_strategy import OverdraftStrategy

class ChequingAccount(BankAccount):
    """
    Represents a chequing account that extends the BankAccount class.
    Chequing accounts are designed for frequent transactions, including both deposits and withdrawals.
    """

    def __init__(self, account_number: int, client_number: int, balance: float, date_created: date, overdraft_limit: float, overdraft_rate: float):
        """
        Initializes the ChequingAccount class.

        Parameters:
            account_number (int): The account number.
            client_number (int): The client number associated with this account.
            balance (float): The initial balance of the account.
            date_created (date): The date the account was created.
            overdraft_limit (float): The maximum overdraft amount before fees apply.
            overdraft_rate (float): The rate at which overdraft fees are applied.
        """
        # Call the parent class initializer
        super().__init__(account_number, client_number, balance, date_created)

        self.__overdraft_limit = overdraft_limit
        self.__overdraft_rate = overdraft_rate
        if not isinstance(date_created, datetime.date):
            raise TypeError("Date created must be a valid date object")
        self._date_created = date_created
        # Initialize the overdraft strategy
        self._overdraft_strategy = OverdraftStrategy(overdraft_limit=self.__overdraft_limit, 
                                             overdraft_rate=self.__overdraft_rate) 
        
        # Validate overdraft limit and overdraft rate
        try:
            self.__overdraft_limit = float(overdraft_limit)
        except ValueError:
            self.__overdraft_limit = -200.0  

        try:
            self.__overdraft_rate = float(overdraft_rate)
        except ValueError:
            self.__overdraft_rate = 0.03 

    # String representation of the ChequingAccount
    def __str__(self):
        """
        Returns a string representation of the ChequingAccount.
        Includes account number, balance, overdraft limit, overdraft rate, and account type.
        """
        return (f"Account Number: {self.account_number} "
                f"Balance: ${self.balance:,.2f}\n"
                f"Overdraft Limit: ${self.__overdraft_limit:,.2f} "
                f"Overdraft Rate: {self.__overdraft_rate * 100:.2f}% "
                f"Account Type: Chequing\n") 


    # Method to calculate service charges
    def get_service_charges(self) -> float:
        """
        Calculates and returns the service charges for the ChequingAccount.
        The service charge is calculated using the _overdraft_strategy.
        """
        return self._overdraft_strategy.calculate_service_charges(self)