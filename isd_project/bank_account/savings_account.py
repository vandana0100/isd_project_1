"""
Description: Unit tests for the SavingsAccount class, which inherits from BankAccount.
Author: Vandana Bhangu

"""
from bank_account.bank_account import BankAccount
from datetime import date
from patterns.strategy.minimum_balance_strategy import MinimumBalanceStrategy

class SavingsAccount(BankAccount):
    SERVICE_CHARGE_PREMIUM: float = 2.0
    BASE_SERVICE_CHARGE: float = 5.0
    
    def __init__(self, account_number: int, client_number: int, balance: float, date_created: date, minimum_balance: float):
        # Call the superclass constructor
        super().__init__(account_number, client_number, balance, date_created)
        self._account_number = account_number
        self._balance = balance 
        self._minimum_balance = minimum_balance
        self._minimum_balance_strategy = MinimumBalanceStrategy(self._minimum_balance)

        # Initialize the MinimumBalanceStrategy with the minimum_balance only
        self._minimum_balance_strategy = MinimumBalanceStrategy(self._minimum_balance)
        
        # Validate the minimum_balance and assign it
        try:
            self._minimum_balance = float(minimum_balance)
        except (ValueError, TypeError):
            self._minimum_balance = 50.0  # Default minimum balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        self._balance = value

    def __str__(self) -> str:
        # Use the superclass __str__ method and add minimum balance and account type
        return (f"{super().__str__()}\n"
                f"Minimum Balance: {self._minimum_balance:.2f} Account Type: Savings")
    
    def get_service_charges(self) -> float:
        """
        Calculates service charges based on the current balance using the MinimumBalanceStrategy.

        Returns:
            float: The calculated service charges.
        """
        if self.balance < self._minimum_balance:
            return self.BASE_SERVICE_CHARGE * self.SERVICE_CHARGE_PREMIUM
        return self.BASE_SERVICE_CHARGE

    
