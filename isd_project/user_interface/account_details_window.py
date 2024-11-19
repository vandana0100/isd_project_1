import os
import sys
from user_interface.details_window import DetailsWindow
from PySide6.QtWidgets import QMessageBox
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from PySide6.QtCore import Signal
from bank_account.bank_account import BankAccount
import copy

class AccountDetailsWindow(DetailsWindow):
    """
    A class used to display account details and perform bank account transactions.
    """
    def __init__(self, account: BankAccount) -> None:
        """
        Initializes a new instance of the ExtendedAccountDetails window.
        Args:
            account: The bank account to be displayed.
        Returns:
            None
        """
        super().__init__()
        self.account = account

        # Ensure the account is an instance of BankAccount
        if isinstance(account, BankAccount):
            self.account = copy.copy(account)  # Make a copy of the bank account

            # Set account number and balance labels
            self.account_number_label.setText(str(self.account.account_number))
            self.balance_label.setText(f"${self.account.balance:.2f}")

            # Connect buttons to their respective methods
            self.deposit_button.clicked.connect(self.on_apply_transaction)
            self.withdraw_button.clicked.connect(self.on_apply_transaction)
            self.exit_button.clicked.connect(self.on_exit)
        else:
            # Reject the window if the account is not an instance of BankAccount
            self.reject()

    def on_apply_transaction(self):
        """
        Handles the deposit or withdrawal transaction.
        If the transaction is valid, it updates the balance. If the transaction fails, shows an error message.
        """
        try:
            # Attempt to convert the amount from the input field
            amount = float(self.transaction_amount_edit.text())
        except ValueError:
            # If the conversion fails, show a message box and exit
            QMessageBox.critical(self, "Deposit Failed", "Invalid amount entered.")
            self.transaction_amount_edit.clear()
            self.transaction_amount_edit.setFocus()
            return

        # Determine which button was clicked (Deposit or Withdraw)
        sender = self.sender()
        transaction_type = ""
        
        if sender == self.deposit_button:
            transaction_type = "Deposit"
            try:
                # Perform the deposit transaction
                self.account.deposit(amount)
                # Update the balance label
                self.balance_label.setText(f"${self.account.balance:.2f}")
                self.transaction_amount_edit.clear()
                self.transaction_amount_edit.setFocus()

                # Emit the signal with the updated account
                self.balance_updated.emit(self.account)

            except Exception as e:
                # Show error message if deposit fails
                QMessageBox.critical(self, "Transaction Failed", f"{transaction_type} failed: {str(e)}")
                self.transaction_amount_edit.clear()
                self.transaction_amount_edit.setFocus()

        elif sender == self.withdraw_button:
            transaction_type = "Withdraw"
            try:
                # Perform the withdrawal transaction
                self.account.withdraw(amount)
                # Update the balance label
                self.balance_label.setText(f"${self.account.balance:.2f}")
                self.transaction_amount_edit.clear()
                self.transaction_amount_edit.setFocus()
                # Emit the signal with the updated account
                self.balance_updated.emit(self.account)
            except Exception as e:
                # Show error message if withdrawal fails
                QMessageBox.critical(self, "Transaction Failed", f"{transaction_type} failed: {str(e)}")
                self.transaction_amount_edit.clear()
                self.transaction_amount_edit.setFocus()

    def exec_(self):
        # Display the window as a dialog
        print(f"Account Details for: {self.account.account_number}")
    

    def on_exit(self):
        """
        Closes the AccountDetailsWindow and returns the user to the previous window.
        """
        self.close()
        
