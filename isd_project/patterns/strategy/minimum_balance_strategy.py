"""
Description: Contains the MinimumBalanceStrategy class for calculating service charges based on minimum balance requirements for savings accounts.
Author: Vandana Bhangu
"""

from patterns.strategy.service_charge_strategy import ServiceChargeStrategy

class MinimumBalanceStrategy(ServiceChargeStrategy):
    """
    Strategy class for calculating service charges based on minimum balance requirements 
    for savings accounts.
    """
    
    def __init__(self, minimum_balance: float, service_charge: float):
        """
        Initializes the MinimumBalanceStrategy with the required minimum balance and service charge.
        
        Parameters:
        minimum_balance (float): The minimum balance that must be maintained in the savings account.
        service_charge (float): The service charge applied if the balance falls below the minimum.
        """
        self._minimum_balance = minimum_balance
        self._service_charge = service_charge

    def calculate_service_charges(self, current_balance: float) -> float:
        """
        Calculates the service charges based on the current balance.
        
        Parameters:
        current_balance (float): The current balance of the savings account.
        
        Returns:
        float: The service charge if the balance is below the minimum; otherwise, returns 0.
        
        Logic:
        - If the current balance is less than the minimum balance, return the service charge.
        - Otherwise, return 0.
        """
        if current_balance < self._minimum_balance:
            return self._service_charge
        return 0.0
