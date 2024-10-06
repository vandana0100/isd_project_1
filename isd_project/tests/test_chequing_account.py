"""
Description: Unit tests for the ChequingAccount class.
Author: ACE Faculty
Modified by: Vandana Bhangu
Date: 05-10-2024
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_chequing_account.py
"""

import unittest
from bank_account.chequing_account import ChequingAccount
from datetime import date

class TestChequingAccount(unittest.TestCase):

    def test_init_valid_values(self):
        # Test Case 1
        account = ChequingAccount(987654321, 1, 1500.00, date(2024, 10, 1), -200.00, 0.03)
        self.assertEqual(account.account_number, 987654321)
        self.assertEqual(account.client_number, 1)
        self.assertEqual(account.balance, 1500.00)
        self.assertEqual(account._ChequingAccount__overdraft_limit, -200.00)
        self.assertEqual(account._ChequingAccount__overdraft_rate, 0.03)

    def test_init_invalid__overdraft_limit(self):
        # Test Case 2
        account = ChequingAccount(987654321, 1, 1500.00, date(2024, 10, 1), 'invalid_limit', 0.03)
        self.assertEqual(account._ChequingAccount__overdraft_limit, -200.00)

    def test_init_invalid__overdraft_rate(self):
        # Test Case 3
        account = ChequingAccount(987654321, 1, 1500.00, date(2024, 10, 1), -200.00, 'invalid_rate')
        self.assertEqual(account._ChequingAccount__overdraft_rate, 0.03)

    def test_init_invalid_date(self):
        # Test Case 4
        with self.assertRaises(TypeError):
            ChequingAccount(987654321, 1, 1500.00, "invalid_date", -200.00, 0.03)

    def test_get_service_charges_balance_above_limit(self):
        # Test Case 5
        account = ChequingAccount(987654321, 1, 1000.00, date(2024, 10, 1), -200.00, 0.03)
        self.assertEqual(account.get_service_charges(), 0.50)

    def test_get_service_charges_balance_below_limit(self):
        # Test Case 6
        account = ChequingAccount(987654321, 1, -300.00, date(2024, 10, 1), -200.00, 0.03)
        self.assertEqual(round(account.get_service_charges(), 2), 3.50)

    def test_get_service_charges_balance_equal_limit(self):
        # Test Case 7
        account = ChequingAccount(987654321, 1, -200.00, date(2024, 10, 1), -200.00, 0.03)
        self.assertEqual(account.get_service_charges(), 0.50)

    def test_str_method(self):
        # Test Case 8
        account = ChequingAccount(987654321, 1, 1500.00, date(2024, 10, 1), -200.00, 0.03)
        expected_str = ("Account Number: 987654321 Balance: $1,500.00\n"
                        "Overdraft Limit: $-200.00 Overdraft Rate: 3.00% Account Type: Chequing\n")
        self.assertEqual(account.__str__(), expected_str)

if __name__ == '__main__':
    unittest.main()
