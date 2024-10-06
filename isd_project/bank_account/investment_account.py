"""
Description: Unit tests for the InvestingAccount class, which inherits from BankAccount.
Author: Vandana Bhangu

"""
from datetime import date, timedelta

class InvestmentAccount:
    """
    Represents an Investment Account for a client.
    
    Attributes:
        BASE_SERVICE_CHARGE (float): The base service charge for the account.
        _account_number (str): The unique identifier for the account.
        _client_number (str): The identifier for the associated client.
        _balance (float): The current balance of the account.
        _date_created (date): The date when the account was created.
    """

    BASE_SERVICE_CHARGE = 10.00

    def __init__(self, account_number, client_number, balance, date_created):
        """
        Initializes the InvestmentAccount instance with provided attributes.

        Args:
            account_number (str): Unique account number.
            client_number (str): Unique client number.
            balance (float): Initial balance of the account.
            date_created (date): Date when the account was created.
        """
        self._account_number = account_number
        self._client_number = client_number
        self._balance = balance
        self._date_created = date_created

    @property
    def account_number(self):
        """Returns the account number."""
        return self._account_number

    @property
    def client_number(self):
        """Returns the client number."""
        return self._client_number

    @property
    def balance(self):
        """Returns the current balance of the account."""
        return self._balance

    @property
    def date_created(self):
        """Returns the date when the account was created."""
        return self._date_created

    @property
    def TEN_YEARS_AGO(self):
        """Calculates the date exactly ten years ago from today."""
        return date.today() - timedelta(days=365 * 10)

    def get_service_charges(self):
        """
        Calculates the service charges based on the date the account was created.

        Returns:
            float: The calculated service charges.
        """
        if self._date_created < self.TEN_YEARS_AGO:
            return self.BASE_SERVICE_CHARGE
        elif self._date_created < date.today():
            return round(self.BASE_SERVICE_CHARGE + 3.00, 2)
        else:
            return 0

    def __str__(self):
        """
        Returns a string representation of the Investment Account details.

        Returns:
            str: A string detailing the account number, balance, service charges, and creation date.
        """
        service_charges = self.get_service_charges()
        return (f"Investment Account {self._account_number} - Balance: {self._balance}, "
                f"Service Charges: {service_charges}, "
                f"Date Created: {self._date_created}")
