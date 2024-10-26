"""
Description: Contains the ManagementFeeStrategy class for calculating management fees 
for investment accounts.
Author: Vandana Bhangu
"""

from patterns.strategy.service_charge_strategy import ServiceChargeStrategy
from datetime import date, timedelta

class ManagementFeeStrategy(ServiceChargeStrategy):
    """
    Strategy class for calculating management fees for investment accounts.
    """
    
    # Constant representing the date ten years ago
    TEN_YEARS_AGO = date.today() - timedelta(days=10 * 365.25)

    def __init__(self, management_fee: float, last_fee_date: date):
        """
        Initializes the ManagementFeeStrategy with a specified management fee 
        and the date of the last fee payment.
        
        Parameters:
        management_fee (float): The fee charged for management of the investment account.
        last_fee_date (date): The date when the last management fee was applied.
        """
        self._management_fee = management_fee
        self._last_fee_date = last_fee_date

    def calculate_service_charges(self, account_creation_date: date) -> float:
        """
        Calculates the service charges based on the account creation date.
        
        Parameters:
        account_creation_date (date): The date when the investment account was created.
        
        Returns:
        float: The calculated management fee if applicable.
        
        Logic:
        - If the account was created more than ten years ago and the last fee date
          is more than one year ago, apply the management fee.
        - Otherwise, no management fee is charged.
        """
        if (account_creation_date < self.TEN_YEARS_AGO) and \
           (self._last_fee_date < date.today() - timedelta(days=365)):
            return self._management_fee
        return 0.0
