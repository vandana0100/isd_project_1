"""
Description: Strategy for calculating overdraft charges.
Author: Vandana Bhangu
"""

from bank_account import BankAccount
from patterns.strategy.service_charge_strategy import ServiceChargeStrategy

class OverdraftStrategy(ServiceChargeStrategy):
    def __init__(self, overdraft_limit: float, overdraft_rate: float): 
        self.overdraft_limit = overdraft_limit
        self.overdraft_rate = overdraft_rate

    def calculate_service_charges(self, account: BankAccount) -> float:
        if account.balance < self.overdraft_limit:
            overdraft_fee = ServiceChargeStrategy.BASE_SERVICE_CHARGE + (self.overdraft_rate * abs(account.balance - self.overdraft_limit))
            return overdraft_fee
        return ServiceChargeStrategy.BASE_SERVICE_CHARGE

    
