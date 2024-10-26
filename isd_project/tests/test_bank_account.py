"""
Description: Unit tests for the BankAccount class.
Author: ACE Faculty
Modified by: Vandana Bhangu
Date: 15-09-2024
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_bank_account.py
"""

import unittest
from bank_account.bank_account import BankAccount

class TestBankAccount(unittest.TestCase):

    def test_init_valid_values(self):
        account = BankAccount(account_number=20204, client_number=10007, balance=2500.75)
        # Expected Results
        self.assertEqual(account.account_number, 20204)
        self.assertEqual(account.client_number, 10007)
        self.assertEqual(round(account.balance, 2), 2500.75)

    def test_init_non_numeric_balance(self):
        # Preconditions
        account = BankAccount(account_number=30305, client_number=20010, balance="invalid_balance")
        
        # Expected Results
        self.assertEqual(account.account_number, 30305)
        self.assertEqual(account.client_number, 20010)
        self.assertEqual(round(account.balance, 2), 0.00)

    def test_init_non_numeric_account_number(self):
        # Preconditions
        with self.assertRaises(ValueError) as context:
            BankAccount(account_number="invalid_account_number", client_number=10020, balance=500.00)
        
        # Expected Results
        self.assertEqual(str(context.exception), "Account number must be an integer.")

    def test_init_non_numeric_client_number(self):
        # Preconditions
        with self.assertRaises(ValueError) as context:
            BankAccount(account_number=67890, client_number="invalid_client_number", balance=1000.00)

        # Expected Results
        self.assertEqual(str(context.exception), "Client number must be an integer.")

    def test_account_number_getter(self):
        # Preconditions
        bank_account = BankAccount(account_number=987654321, client_number=54321, balance=2500.75)
        
        # Method Inputs
        actual_account_number = bank_account.account_number
        
        # Expected Results
        self.assertEqual(actual_account_number, 987654321, f"Expected 987654321, but got {actual_account_number}")

    def test_client_number_getter(self):
        # Preconditions
        bank_account = BankAccount(account_number=923476, client_number=476599, balance=3000.00)
        
        # Method Inputs
        actual_client_number = bank_account.client_number
        
        # Expected Results
        self.assertEqual(actual_client_number, 476599, f"Expected 476599, but got {actual_client_number}")

    def test_balance_getter(self):
        # Preconditions
        bank_account = BankAccount(account_number=562309, client_number=873452, balance=1500.75)
        
        # Method Inputs
        actual_balance = bank_account.balance
        
        # Expected Results
        self.assertEqual(round(actual_balance, 2), 1500.75, f"Expected 1500.75, but got {actual_balance}")

    def test_update_balance_positive_amount(self):
        # Preconditions
        bank_account = BankAccount(account_number=509709, client_number=898652, balance=1501.00)
        
        # Method Inputs
        bank_account.update_balance(237.00)
        
        # Expected Results
        self.assertEqual(round(bank_account.balance, 2), 1738.00, f"Expected balance to be 1738.00, but got {bank_account.balance}")

    def test_update_balance_negative_amount(self):
        # Preconditions
        bank_account = BankAccount(account_number=873422, client_number=868952, balance=5000.00)
        
        # Method Inputs
        bank_account.update_balance(-1234.00)
        
        # Expected Results
        self.assertEqual(round(bank_account.balance, 2), 3766.00, f"Expected balance to be 3766.00, but got {bank_account.balance}")

    def test_update_balance_non_numeric_amount(self):
        # Preconditions
        bank_account = BankAccount(account_number=875764, client_number=229802, balance=2000.00)
        
        # Method Inputs
        try:
            bank_account.update_balance("non-numeric")
        except ValueError:
            pass  # Expect a ValueError to be raised
        
        # Expected Results
        self.assertEqual(round(bank_account.balance, 2), 2000.00, f"Expected balance to be 2000.00, but got {bank_account.balance}")

    def test_deposit_valid_amount(self):
        # Preconditions
        bank_account = BankAccount(account_number=809344, client_number=669902, balance=1500.00)
        
        # Method Inputs
        bank_account.deposit(250.00)
        
        # Expected Results
        self.assertEqual(round(bank_account.balance, 2), 1750.00, f"Expected balance to be 1750.00, but got {bank_account.balance}")

    def test_deposit_negative_amount(self):
        # Preconditions
        bank_account = BankAccount(account_number=982357, client_number=985648, balance=1200.00)
        
        # Method Inputs and Expected Results
        with self.assertRaises(ValueError) as context:
            bank_account.deposit(-150.00)
        
        self.assertEqual(str(context.exception), "Deposit amount: -150.00 must be positive.")

    def test_withdraw_valid_amount(self):
        # Preconditions
        bank_account = BankAccount(account_number=674523, client_number=674312, balance=1500.00)
        
        # Method Inputs
        bank_account.withdraw(200.00)
        
        # Expected Results
        self.assertEqual(round(bank_account.balance, 2), 1300.00, "The balance should be updated to 1300.00 after withdrawal.")

    def test_withdraw_negative_amount_alternate(self):
        # Preconditions
        bank_account = BankAccount(account_number=432189, client_number=567891, balance=1500.00)
        
        # Method input: withdraw negative amount
        with self.assertRaises(ValueError) as context:
            bank_account.withdraw(-75.00)
        
        # Expected exception message
        expected_message = "Withdrawal amount: -75.00 must be positive."
        
        # Check if ValueError is raised with correct message
        self.assertEqual(str(context.exception), expected_message, f"Expected ValueError message to be '{expected_message}', but got '{str(context.exception)}'.")
    
    def test_withdraw_exceeds_balance(self):
        # Preconditions
        bank_account = BankAccount(account_number=984743, client_number=493686, balance=200.00)
        
        # Method Inputs and Expected Results
        with self.assertRaises(ValueError) as context:
            bank_account.withdraw(300.00)
        
        # Check the exception message
        self.assertEqual(str(context.exception), "Withdrawal amount: 300.00 must not exceed the account balance: 200.00", "Expected ValueError not raised for withdraw amount exceeding balance.")
        
        # Ensure the balance remains unchanged
        self.assertEqual(round(bank_account.balance, 2), 200.00, "The balance should remain unchanged at 200.00.")

    def test_str_method(self):
        # Preconditions
        bank_account = BankAccount(account_number=966643, client_number=493222, balance=1234.56)
    
        # Expected string output including the newline character
        expected_output = "Account Number: 966643 Balance: $1,234.56\n"
    
        # Assert that the __str__ method returns the correct output
        self.assertEqual(str(bank_account), expected_output)

if __name__ == '__main__':
    unittest.main()
