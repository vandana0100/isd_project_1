"""
Description: Contains the base class for service charge calculation strategies.
Author: Vandana Bhangu
"""

from abc import ABC, abstractmethod
from bank_account import BankAccount

class ServiceChargeStrategy(ABC):
    BASE_SERVICE_CHARGE: float = 0.50

    @abstractmethod
    def calculate_service_charges(self, account: BankAccount) -> float:
        """
        Abstract method for calculating service charges.
        :param account: BankAccount object
        :return: Calculated service charge as a float
        """
        pass
