"""
Description: Unit tests for the SavingsAccount class.
Author: ACE Faculty
Modified by: Vandana Bhangu
Date: 05-10-2024
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_savings_account.py
"""
import unittest
from bank_account.savings_account import SavingsAccount
from datetime import date
from patterns.strategy.minimum_balance_strategy import MinimumBalanceStrategy

class TestSavingsAccount(unittest.TestCase):

    def setUp(self):
        # This method will run before each test
        self.account = SavingsAccount(
            account_number=9483914,
            client_number=123456,
            balance=1000.0,
            date_created=date.today(),
            minimum_balance=50.0
        )

    def test_init_attributes(self):
        # Test to ensure attributes are set correctly
        self.assertEqual(self.account.account_number, 9483914)
        self.assertEqual(self.account.client_number, 123456)
        self.assertEqual(round(self.account.balance, 2), 1000.0)
        self.assertEqual(self.account._minimum_balance, 50.0)
        self.assertEqual(self.account._minimum_balance, 50.0)
        self.assertIsInstance(self.account._minimum_balance_strategy, MinimumBalanceStrategy)


    def test_init_invalid_minimum_balance(self):
        # Test to check minimum_balance is set to default when invalid type is provided
        account = SavingsAccount(9483914, 123456, 1000.0, date.today(), "invalid")
        self.assertEqual(account._minimum_balance, 50.0)

    def test_get_service_charges_balance_greater_than_minimum(self):
        # Test when balance is greater than minimum balance
        self.assertEqual(round(self.account.get_service_charges(), 2), round(self.account.BASE_SERVICE_CHARGE, 2))

    def test_get_service_charges_balance_equal_to_minimum(self):
        # Test when balance equals minimum balance
        self.account.balance = 50.0
        self.assertEqual(round(self.account.get_service_charges(), 2), round(self.account.BASE_SERVICE_CHARGE, 2))

    def test_get_service_charges_balance_less_than_minimum(self):
        # Test when balance is less than minimum balance
        self.account.balance = 49.99
        expected_service_charge = round(self.account.BASE_SERVICE_CHARGE * self.account.SERVICE_CHARGE_PREMIUM, 2)
        self.assertEqual(round(self.account.get_service_charges(), 2), expected_service_charge)

    def test_str_method(self):
        # Test __str__ method for correct string representation
        expected_str = (f"Account Number: {self.account.account_number} Balance: ${self.account.balance:.2f}\n"
                f"Minimum Balance: {self.account._minimum_balance:.2f} Account Type: Savings")
        

if __name__ == '__main__':
    unittest.main()
