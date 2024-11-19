"""
Description: This module defines the Client class with attributes for client number, first name, last name, and email address.
It implements the Observer pattern to receive notifications for significant activities in bank accounts.
Author: Vandana Bhangu
"""

from email_validator import validate_email, EmailNotValidError
import client
from utility.file_utils import simulate_send_email
from patterns.observer.observer import Observer 

class Client:
    def __init__(self, client_number: int, first_name: str, last_name: str, email_address: str):
        # Validate client_number
        if not isinstance(client_number, int):
            raise ValueError("Client number must be an integer.")
        self.__client_number = client_number

        

        # Validate first_name
        first_name = first_name.strip()
        if not first_name:
            raise ValueError("First name cannot be blank.")
        self.__first_name = first_name

        # Validate last_name
        last_name = last_name.strip()
        if not last_name:
            raise ValueError("Last name cannot be blank.")
        self.__last_name = last_name

        # Validate email_address
        try:
            valid_email = validate_email(email_address).email
            self.__email_address = valid_email
        except EmailNotValidError:
            # Fallback email if validation fails
            self.__email_address = "email@yahoo.com"

    # Property for client_number
    @property
    def client_number(self) -> int:
        return self.__client_number

    # Property for first_name
    @property
    def first_name(self) -> str:
        return self.__first_name

    # Property for last_name
    @property
    def last_name(self) -> str:
        return self.__last_name

    # Property for email_address
    @property
    def email_address(self) -> str:
        return self.__email_address
    
    def __str__(self):
        return f"Client {self.client_number}: {self.first_name} {self.last_name}, Email: {self.email_address}"
    
    def update(self, message: str) -> None:
        """
        Update method to handle notifications from the subject.
        Sends a simulated email notification to the client.

        :param message: The notification message to be sent.
        """
        from datetime import datetime

        # Format the subject and message
        subject = f"ALERT: Unusual Activity: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        formatted_message = f"Notification for {self.client_number}: {self.first_name} {self.last_name}: {message}"

        # Simulate sending email
        simulate_send_email(self.email_address, subject, formatted_message)


