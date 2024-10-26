"""
Description: Contains the OverdraftStrategy class for calculating service charges 
related to overdrafts.
Author: Vandana Bhangu
"""

from patterns.strategy.service_charge_strategy import ServiceChargeStrategy

class OverdraftStrategy(ServiceChargeStrategy):
    """
    Strategy class for calculating service charges when an account is overdrawn.
    """

    def __init__(self, overdraft_fee: float):
        """
        Initializes the OverdraftStrategy with a specified overdraft fee.
        
        Parameters:
        overdraft_fee (float): The fee charged when the account balance is negative.
        """
        self._overdraft_fee = overdraft_fee

    def calculate_service_charges(self, balance: float) -> float:
        """
        Calculates the service charges based on the account balance.
        
        Parameters:
        balance (float): The current balance of the account.
        
        Returns:
        float: The calculated service charge.
        
        Logic:
        - If the balance is negative, apply the overdraft fee.
        - If the balance is positive or zero, there is no overdraft fee.
        """
        if balance < 0:
            return self._overdraft_fee
        return 0.0
