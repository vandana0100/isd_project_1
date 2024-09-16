"""
Description: Unit tests for the Client class.
Author: ACE Faculty
Modified by: Vandana Bhangu
Date: 15-09-2024
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests.test_client.py
"""
import unittest
from client.client import Client  

class TestClient(unittest.TestCase):

    def test_client_init_valid_values(self):
        client = Client(client_number=98765, first_name="Charlie", last_name="Brown", email_address="charlie.brown@yahoo.com")
        
        self.assertEqual(client.client_number, 98765)
        self.assertEqual(client.first_name, "Charlie")
        self.assertEqual(client.last_name, "Brown")
        self.assertEqual(client.email_address, "charlie.brown@yahoo.com")

    def test_invalid_client_number(self):
        # Define the test case inputs
        client_number = "invalid" 
        first_name = "Mohan"
        last_name = "Kumar"
        email_address = "mohan.kumar@yahoo.com"
        
        # Check if ValueError is raised with the correct message
        with self.assertRaises(ValueError) as context:
            Client(client_number, first_name, last_name, email_address)
        
        self.assertEqual(str(context.exception), "Client number must be an integer.")

    def test_blank_first_name(self):
        # Define the test case inputs
        client_number = 456  # Valid client number
        first_name = "   "  # Blank first name with spaces
        last_name = "Singh"  # Valid last name
        email_address = "singh@example.com"  # Valid email address
        
        # Check if ValueError is raised with the correct message
        with self.assertRaises(ValueError) as context:
            Client(client_number, first_name, last_name, email_address)
        
        self.assertEqual(str(context.exception), "First name cannot be blank.")

    def test_blank_last_name(self):
        with self.assertRaises(ValueError) as context:
            Client(4567, "Bhavesh", "", "bhavesh@yahoo.com")

        self.assertEqual(str(context.exception), "Last name cannot be blank.")

    def test_invalid_email_address(self):
        client = Client(7890, "Jaspreet", "Singh", "invalid-email")
        # Access the private attribute using name mangling
        self.assertEqual(client._Client__email_address, "email@yahoo.com")
    
    def test_client_number_property(self):
        client = Client(client_number=45678, first_name="Harpreet", last_name="Kaur", email_address="harpreet.kaur@yahoo.com")
        # Check if client_number returns the correct value
        self.assertEqual(client.client_number, 45678, f"Expected 45678, but got {client.client_number}")

    def test_first_name_property(self):
        client = Client(client_number=78901, first_name="Gurpreet", last_name="Singh", email_address="gurpreet.singh@yahoo.com")
        
        # Check if first_name returns the correct value
        self.assertEqual(client.first_name, "Gurpreet", f"Expected 'Gurpreet', but got {client.first_name}")

    def test_last_name_property(self):
        client = Client(client_number=34567, first_name="Manpreet", last_name="Gill", email_address="manpreet.gill@yahoo.com")
        
        # Check if last_name returns the correct value
        self.assertEqual(client.last_name, "Gill", f"Expected 'Gill', but got {client.last_name}")

    def test_email_address_property(self):
        client = Client(client_number=67890, first_name="Sukhdeep", last_name="Singh", email_address="sukhdeep.singh@yahoo.com")
        
        # Check if email_address returns the correct value
        self.assertEqual(client.email_address, "sukhdeep.singh@yahoo.com", f"Expected 'sukhdeep.singh@yahoo.com', but got {client.email_address}")

    def test_str_method(self):
        client = Client(client_number=56777, first_name="Gagandeep", last_name="Singh", email_address="gagandeep.singh@yahoo.com")
        
        # Check if the __str__ method returns the correct format
        expected_str = "Singh, Gagandeep [56777] - gagandeep.singh@yahoo.com\n"
        self.assertEqual(str(client), expected_str, f"Expected '{expected_str}', but got '{str(client)}'")

if __name__ == '__main__':
    unittest.main()
