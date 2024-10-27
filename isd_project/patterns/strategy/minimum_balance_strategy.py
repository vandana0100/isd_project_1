"""
Description: Strategy for calculating charges based on minimum balance requirements.
Author: Vandana Bhangu
"""

from bank_account import BankAccount
from patterns.strategy.service_charge_strategy import ServiceChargeStrategy
from bank_account.bank_account import BankAccount


class MinimumBalanceStrategy(ServiceChargeStrategy):
    SERVICE_CHARGE_PREMIUM: float = 2.0

    def __init__(self, minimum_balance: float):
        self.minimum_balance = minimum_balance

    def calculate_service_charges(self, account: BankAccount) -> float:
        if account.balance < self.minimum_balance:
            return ServiceChargeStrategy.BASE_SERVICE_CHARGE * MinimumBalanceStrategy.SERVICE_CHARGE_PREMIUM
        return ServiceChargeStrategy.BASE_SERVICE_CHARGE
    


