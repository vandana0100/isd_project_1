"""
Description: Contains the base class for service charge calculation strategies.
Author: Vandana Bhangu
"""

from abc import ABC, abstractmethod

class ServiceChargeStrategy(ABC):
    """
    Abstract base class for service charge strategies. Provides a blueprint
    for calculating service charges based on different strategies.
    """

    # Constants (can be moved from the BankAccount class if needed)
    MINIMUM_BALANCE = 1000.0
    LOW_BALANCE_FEE = 25.0

    @abstractmethod
    def calculate_service_charges(self, balance: float) -> float:
        """
        Abstract method to calculate service charges.

        Parameters:
        balance (float): The current balance of the account.

        Returns:
        float: The calculated service charge.
        """
        pass
