"""
Description: Unit tests for the InvestingAccount class.
Author: ACE Faculty
Modified by: Vandana Bhangu
Date: 05-10-2024
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_investment_account.py
"""

import unittest
from datetime import date, timedelta
from bank_account.investment_account import InvestmentAccount

class TestInvestmentAccount(unittest.TestCase):
    
    def setUp(self):
        # Create an account with a known creation date
        self.account = InvestmentAccount("123456", "78910", 1000.00, date(2022, 1, 1))
        self.base_service_charge = InvestmentAccount.BASE_SERVICE_CHARGE
    
    def test_get_service_charges_exactly_ten_years(self):
        # Account created exactly 10 years ago
        self.account._date_created = date.today() - timedelta(days=365 * 10)
        self.assertEqual(self.account.get_service_charges(), round(self.base_service_charge + 3.00, 2))

    def test_get_service_charges_older_than_ten_years(self):
        # Account created more than 10 years ago
        self.account._date_created = date.today() - timedelta(days=365 * 11)
        self.assertEqual(self.account.get_service_charges(), self.base_service_charge)

    def test_get_service_charges_within_ten_years(self):
        # Account created within the last 10 years
        self.account._date_created = date.today() - timedelta(days=365 * 5)
        self.assertEqual(self.account.get_service_charges(), round(self.base_service_charge + 3.00, 2))

    def test_get_service_charges_new_account(self):
        # Account created today
        self.account._date_created = date.today()
        self.assertEqual(self.account.get_service_charges(), 0)

    def test_str_management_fee(self):
        # Test string representation of an account that includes the management fee
        self.account._date_created = date.today() - timedelta(days=365 * 5)  # Within 10 years
        expected_output = (f"Investment Account {self.account.account_number} - Balance: {self.account.balance}, "
                           f"Service Charges: {round(self.base_service_charge + 3.00, 2)}, "
                           f"Date Created: {self.account.date_created}")
        self.assertEqual(str(self.account), expected_output)

    def test_str_waived_management_fee(self):
        # Test string representation of an account with a waived management fee
        self.account._date_created = date.today() - timedelta(days=365 * 11)  # More than 10 years
        expected_output = (f"Investment Account {self.account.account_number} - Balance: {self.account.balance}, "
                           f"Service Charges: {self.base_service_charge}, "
                           f"Date Created: {self.account.date_created}")
        self.assertEqual(str(self.account), expected_output)

    def test_str_today_account(self):
        # Test string representation of an account created today (no charges)
        self.account._date_created = date.today()
        expected_output = (f"Investment Account {self.account.account_number} - Balance: {self.account.balance}, "
                           f"Service Charges: 0, "
                           f"Date Created: {self.account.date_created}")
        self.assertEqual(str(self.account), expected_output)

if __name__ == '__main__':
    unittest.main()

