from PySide6.QtWidgets import QTableWidgetItem, QMessageBox
from PySide6.QtCore import Qt
from PySide6.QtCore import Slot
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from user_interface.lookup_window import LookupWindow
from user_interface.account_details_window import AccountDetailsWindow
from user_interface.manage_data import load_data
from user_interface.manage_data import update_data
from bank_account.bank_account import BankAccount

class ClientLookupWindow(LookupWindow):
    """
    Description: This class handles the client lookup functionality within the banking application.
    It allows the user to search for a client by their client number and view their associated accounts.
    Author: Vandana Bhangu
    """
    
    def __init__(self):
        super().__init__()
        # Initialize widgets, layout, and load data
        self.client_listing, self.accounts = load_data()

        # Debugging: Print loaded data
        print(f"Loaded client_listing: {self.client_listing}")  # Check the client_listing data

        # Connect signals to slots
        self.lookup_button.clicked.connect(self.on_lookup_client)
        self.account_table.cellClicked.connect(self.__on_select_account)
        self.filter_button.clicked.connect(self.on_apply_filter)  # Connect filter button to the apply filter method

        # Add a variable to track the applied filter state
        self.filter_applied = False

    @Slot()
    def on_lookup_client(self):
        """
        This method handles the client lookup process. It retrieves the client number from the input field, 
        checks if it's valid and exists, and displays the associated client and account information.
        """
        # Check if the client number is valid (numeric)
        try:
            client_number = int(self.client_number_edit.text())  # Get the client number from the input field
        except ValueError:
            QMessageBox.warning(self, "Non-Numeric Client", "Client number must be numeric.")  # Error for non-numeric input
            self.reset_display()  # Clear previous data
            return  # Exit the method early, as no further processing is needed
        
        # Check if the client exists in the client listing
        if client_number not in self.client_listing:
            print(f"Client number {client_number} not found in client_listing.")  # Debug print
            QMessageBox.warning(self, "Client Not Found", f"Client with number {client_number} not found.")
            self.reset_display()  # Clear previous data
            return 
        else:
            # Invoke the toggle_filter method to indicate that the data is not currently filtered
            self.toggle_filter(False)
            
        # Display client information
        client = self.client_listing[client_number]
        self.client_info_label.setText(f"Client Found: {client.first_name} {client.last_name}")

        # Populate the account table with the client's accounts
        self.account_table.setRowCount(0)  # Clear previous rows
        for account in self.accounts.values():
            if account.client_number == client_number:
                row = self.account_table.rowCount()
                self.account_table.insertRow(row)
                
                # Insert account details in table columns
                self.account_table.setItem(row, 0, QTableWidgetItem(str(account.account_number)))
                self.account_table.setItem(row, 1, QTableWidgetItem(f"${account.balance:,.2f}"))
                self.account_table.setItem(row, 2, QTableWidgetItem(account._date_created.strftime("%Y-%m-%d")))
                self.account_table.setItem(row, 3, QTableWidgetItem(account.__class__.__name__))
        
        self.account_table.resizeColumnsToContents()

    @Slot(int, int)
    def __on_select_account(self, row: int, column: int) -> None:
        """
        Slot method that handles the selection of an account from the table.
        If a valid account is selected, it opens the AccountDetailsWindow.
        If the account is invalid or empty, it shows an error message.
        
        Args:
            row (int): The row number of the selected cell.
            column (int): The column number of the selected cell.
        """
        # Assuming account_number is in the first column (column 0)
        account_number = self.account_table.item(row, 0).text()
    

        if not account_number:
            # If the account number is blank, show a message box to select a valid record
            QMessageBox.warning(self, "Invalid Selection", "Please select a valid record.")
            return

        # Check if the account number exists in the accounts dictionary
        if account_number in self.accounts:
            # Get the BankAccount object for the selected account
            account = self.accounts[account_number]

            # Create an instance of AccountDetailsWindow and pass the BankAccount object
            account_details_window = AccountDetailsWindow(account)
            
            # Show the AccountDetailsWindow as a dialog box
            account_details_window.exec_()
        else:
            # If the account does not exist in the dictionary, show an error message
            QMessageBox.critical(self, "Account Not Found", "Bank account selected does not exist.")

    def show_message(self, title: str, message: str) -> None:
        """
        Helper method to show a QMessageBox with the provided title and message.
        
        Arguments:
        - title: The title of the message box.
        - message: The message to be displayed in the message box.
        """
        msg_box = QMessageBox()
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.exec_()
    
    def reset_display(self):
        """
        This method resets the display, clearing the client information and the account table.
        """
        self.client_info_label.clear()
        self.account_table.setRowCount(0)
        self.filter_edit.clear()

    def toggle_filter(self, filter_on: bool) -> None:
        """
        This method toggles the display of the filter widgets to indicate to the user 
        whether or not filtering is currently taking place.
        
        Arguments:
        - filter_on: Boolean indicating if filtering is on or not.
        """
        if filter_on:
            self.filter_button.setText("Reset")
            self.filter_combo_box.setEnabled(False)
            self.filter_edit.setEnabled(False)
            self.filter_label.setText("Data is Currently Filtered")
        else:
            self.filter_button.setText("Apply Filter")
            self.filter_combo_box.setEnabled(True)
            self.filter_edit.setEnabled(True)
            self.filter_edit.clear()
            self.filter_combo_box.setCurrentIndex(0)
            self.filter_label.setText("Data is Not Currently Filtered")
            # Display all rows in the table
            for row in range(self.account_table.rowCount()):
                self.account_table.setRowHidden(row, False)

    @Slot()
    def on_apply_filter(self):
        """
        This method applies the filter to the accounts table based on the selected account type 
        and filter criteria (e.g., balance or account number).
        """
        filter_value = self.filter_edit.text().strip()
        filter_type = self.filter_combo_box.currentText().strip()

        if not filter_value:
            QMessageBox.warning(self, "Invalid Filter", "Please enter a valid filter value.")
            return  # Exit early if the filter value is invalid

        if filter_type == "Account Type":
            self.apply_account_type_filter(filter_value)
        elif filter_type == "Balance":
            self.apply_balance_filter(filter_value)
        else:
            QMessageBox.warning(self, "Invalid Filter Type", "Please select a valid filter type.")
            return
        
        # Toggle the filter status
        self.filter_applied = True
        self.toggle_filter(True)

    def apply_account_type_filter(self, account_type: str):
        """
        Apply a filter on account type (e.g., Savings, Checking).
        """
        filter_found = False
        for row in range(self.account_table.rowCount()):
            account_number = self.account_table.item(row, 0).text()
            account = self.accounts.get(account_number)

            if account and account.__class__.__name__ != account_type:
                self.account_table.setRowHidden(row, True)  # Hide rows that don't match the filter
            else:
                self.account_table.setRowHidden(row, False)  # Show rows that match the filter
                filter_found = True  # At least one match was found

        # If no matches are found, show a message box
        if not filter_found:
            QMessageBox.warning(self, "No Matches Found", f"No accounts of type {account_type} found.")

    def apply_balance_filter(self, balance_threshold: str):
        """
        Apply a filter based on the account balance.
        """
        try:
            balance_threshold = float(balance_threshold)
            filter_found = False
            for row in range(self.account_table.rowCount()):
                account_number = self.account_table.item(row, 0).text()
                account = self.accounts.get(account_number)

                if account and account.balance < balance_threshold:
                    self.account_table.setRowHidden(row, True)  # Hide rows that don't match the filter
                else:
                    self.account_table.setRowHidden(row, False)  # Show rows that match the filter
                    filter_found = True  # At least one match was found

            # If no matches are found, show a message box
            if not filter_found:
                QMessageBox.warning(self, "No Matches Found", f"No accounts with balance above {balance_threshold} found.")
        except ValueError:
            QMessageBox.warning(self, "Invalid Balance", "Please enter a valid numeric balance value.")

    @Slot()
    def on_reset_filter(self):
        """
        This method resets the applied filter, clears the filter field, 
        and makes all rows visible again.
        """
        # Reset filter fields
        self.filter_edit.clear()
        self.filter_combo_box.setCurrentIndex(0)
        
        # Show all rows again
        for row in range(self.account_table.rowCount()):
            self.account_table.setRowHidden(row, False)

        # Toggle the filter status
        self.filter_applied = False
        self.toggle_filter(False)
