"""
Description: Strategy for applying management fees to a bank account.
Author: Vandana Bhangu
"""

from datetime import date, timedelta
from bank_account import BankAccount
from .service_charge_strategy import ServiceChargeStrategy

class ManagementFeeStrategy(ServiceChargeStrategy):
    TEN_YEARS_AGO: date = date.today() - timedelta(days=3650)

    def __init__(self, date_created: date, management_fee: float):
        self.date_created = date_created
        self.management_fee = management_fee

    def calculate_service_charges(self, account: BankAccount) -> float:
        if self.date_created < ManagementFeeStrategy.TEN_YEARS_AGO:
            return max(ServiceChargeStrategy.BASE_SERVICE_CHARGE, self.management_fee / 2)
        return max(ServiceChargeStrategy.BASE_SERVICE_CHARGE, self.management_fee)

