"""
Description: A client program written to verify implementation 
of the Observer Pattern.
Author: ACE Faculty
Edited by: Vandana Bhangu
Date: 27-10-2024
"""

# 1.  Import all BankAccount types using the bank_account package
#     Import date
#     Import Client
from bank_account import BankAccount, ChequingAccount, SavingsAccount
from client.client import Client
from client.client import Client
from datetime import date

def main():


# 2. Create a Client object with data of your choice.
    try:
        client1 = Client(1967, "Annie", "Gold", "annie.gold@yahoo.com")
        print(f"Client created: {client1}")
    except ValueError as e:
        print(f"Error creating client: {e}")

# 3a. Create a ChequingAccount object with data of your choice, using the client_number 
# of the client created in step 2.
    try:
        chequing_account = ChequingAccount(200999, client1.client_number, balance=1500.0, date_created=date.today(), overdraft_limit=500.0, overdraft_rate=0.03)
        print(f"Chequing account created: {chequing_account}")
    except ValueError as e:
        print(f"Error creating chequing account: {e}")

# 3b. Create a SavingsAccount object with data of your choice, using the client_number 
# of the client created in step 2.
    try:
        savings_account = SavingsAccount(200222, client1.client_number, balance=2000.0, date_created=date.today(), minimum_balance=500.0)
        print(f"Savings account created: {savings_account}")
    except ValueError as e:
        print(f"Error creating savings account: {e}")


# 4 The ChequingAccount and SavingsAccount objects are 'Subject' objects.
# The Client object is an 'Observer' object.  
# 4a.  Attach the Client object (created in step 1) to the ChequingAccount object (created in step 2).
# 4a.  Attach the Client object (created in step 1) to the SavingsAccount object (created in step 2).
    try:
        chequing_account.subscribe(client1)
    except Exception as e:
        print(f"Error attaching client to chequing account: {e}")

    try:
        savings_account.subscribe(client1)
    except Exception as e:
        print(f"Error attaching client to savings account: {e}")


# 5a. Create a second Client object with data of your choice.
    try:
        client2 = Client(1453, "Bunny", "loth", "bunny.loth@yahoo.com")
        print(f"Second client created: {client2}")
    except ValueError as e:
        print(f"Error creating second client: {e}")

# 5b. Create a SavingsAccount object with data of your choice, using the client_number 
# of the client created in this step.
    try:
        savings_account2 = SavingsAccount(200686, client2.client_number, balance=3000.00, date_created=date.today(), minimum_balance=500.0)
        print(f"Second savings account created: {savings_account2}")
    except ValueError as e:
        print(f"Error creating second savings account: {e}")


# 6. Use the ChequingAccount and SavingsAccount objects created 
# in steps 3 and 5 above to perform transactions (deposits and withdraws) 
# which would cause the Subject (BankAccount) to notify the Observer 
# (Client) as well as transactions that would not 
# cause the Subject to notify the Observer.  Ensure each 
# BankAccount object performs at least 3 transactions.
# REMINDER: the deposit() and withdraw() methods can raise exceptions
# ensure the methods are invoked using proper exception handling such 
# that any exception messages are printed to the console.
    # Transactions for ChequingAccount
    try:
        chequing_account.deposit(2000)  
        chequing_account.withdraw(500)  
        chequing_account.withdraw(200)  
    except ValueError as e:
        print(f"Error performing transaction on chequing account: {e}")

    # Transactions for SavingsAccount
    try:
        savings_account.deposit(500)  
        savings_account.withdraw(200)  
        savings_account.withdraw(1500)  
    except ValueError as e:
        print(f"Error performing transaction on savings account: {e}")

    # Transactions for second SavingsAccount
    try:
        savings_account2.deposit(1000) 
        savings_account2.withdraw(2500)  
        savings_account2.withdraw(50)  
    except ValueError as e:
        print(f"Error performing transaction on second savings account: {e}")

if __name__ == "__main__":
    main()


