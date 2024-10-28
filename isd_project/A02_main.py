"""
Description: A client program written to verify correctness of 
the BankAccount sub classes.
Author: ACE Faculty
Edited by: Vandana Bhangu
Date: 06-10-2024
Latest Update: 27-10-2024
"""

# 1.  Import all BankAccount types using the bank_account package
#     Import date from datetime
from datetime import date
from bank_account.chequing_account import ChequingAccount
from bank_account.investment_account import InvestmentAccount
from bank_account.savings_account import SavingsAccount


# 2. Create an instance of a ChequingAccount with values of your 
# choice including a balance which is below the overdraft limit.
try:
    chequing_account = ChequingAccount(account_number=567345, client_number=789, balance=-200, overdraft_limit=-500, date_created=date.today(), overdraft_rate=0.05)  
except Exception as e:
    print(f"Error creating ChequingAccount: {e}")


# 3. Print the ChequingAccount created in step 2.
try:
    print(chequing_account)
except Exception as e:
    print(f"Error printing ChequingAccount: {e}")

# 3b. Print the service charges amount if calculated based on the 
# current state of the ChequingAccount created in step 2.
try:
    print(f"Service charges: ${chequing_account.get_service_charges():.2f}")
except Exception as e:
    print(f"Error calculating service charges: {e}")


# 4a. Use ChequingAccount instance created in step 2 to deposit 
# enough money into the chequing account to avoid overdraft fees.
try:
    chequing_account.deposit(300)
except Exception as e:
    print(f"Error depositing into ChequingAccount: {e}")

# 4b. Print the ChequingAccount
try:
    print(chequing_account)
except Exception as e:
    print(f"Error printing ChequingAccount: {e}")

# 4c. Print the service charges amount if calculated based on the 
# current state of the ChequingAccount created in step 2.
try:
    print(f"Service charges: ${chequing_account.get_service_charges():.2f}")
except Exception as e:
    print(f"Error calculating service charges: {e}")

print("===================================================")


# 5. Create an instance of a SavingsAccount with values of your 
# choice including a balance which is above the minimum balance.
try:
    savings_account = SavingsAccount(account_number=654321, client_number=456, balance=2000, minimum_balance=1000,  date_created=date.today())
except Exception as e:
    print(f"Error creating SavingsAccount: {e}")


# 6. Print the SavingsAccount created in step 5.
try:
    print(savings_account)
except Exception as e:
    print(f"Error printing SavingsAccount: {e}")

# 6b. Print the service charges amount if calculated based on the 
# current state of the SavingsAccount created in step 5.
try:
    print(f"Service charges: ${savings_account.get_service_charges():.2f}")
except Exception as e:
    print(f"Error calculating service charges: {e}")


# 7a. Use this SavingsAccount instance created in step 5 to withdraw 
# enough money from the savings account to cause the balance to fall 
# below the minimum balance.
try:
    savings_account.withdraw(1200)
except Exception as e:
    print(f"Error withdrawing from SavingsAccount: {e}")

# 7b. Print the SavingsAccount.
try:
    print(savings_account)
except Exception as e:
    print(f"Error printing SavingsAccount: {e}")

# 7c. Print the service charges amount if calculated based on the 
# current state of the SavingsAccount created in step 5.
try:
    print(f"Service charges: ${savings_account.get_service_charges():.2f}")
except Exception as e:
    print(f"Error calculating service charges: {e}")

print("===================================================")

# 8. Create an instance of an InvestmentAccount with values of your 
# choice including a date created within the last 10 years.
try:
    investment_account_recent = InvestmentAccount(account_number=987654, client_number=321, balance=5000, date_created=date(2018, 6, 15))
except Exception as e:
    print(f"Error creating InvestmentAccount (recent): {e}")


# 9a. Print the InvestmentAccount created in step 8.
try:
    print(investment_account_recent)
except Exception as e:
    print(f"Error printing InvestmentAccount: {e}")

# 9b. Print the service charges amount if calculated based on the 
# current state of the InvestmentAccount created in step 8.
try:
    print(f"Service charges: ${investment_account_recent.get_service_charges():.2f}")
except Exception as e:
    print(f"Error calculating service charges: {e}")


# 10. Create an instance of an InvestmentAccount with values of your 
# choice including a date created prior to 10 years ago.
try:
    investment_account_old = InvestmentAccount(account_number=567890, client_number=654, balance=10000, date_created=date(2005, 3, 10))
except Exception as e:
    print(f"Error creating InvestmentAccount (old): {e}")


# 11a. Print the InvestmentAccount created in step 10.
try:
    print(investment_account_old)
except Exception as e:
    print(f"Error printing InvestmentAccount: {e}")

# 11b. Print the service charges amount if calculated based on the 
# current state of the InvestmentAccount created in step 10.
try:
    print(f"Service charges: ${investment_account_old.get_service_charges():.2f}")
except Exception as e:
    print(f"Error calculating service charges: {e}")

print("===================================================")


# 12. Update the balance of each account created in steps 2, 5, 8 and 10 
# by using the withdraw method of the superclass and withdrawing 
# the service charges determined by each instance invoking the 
# polymorphic get_service_charges method.
try:
    chequing_account.withdraw(chequing_account.get_service_charges())
    savings_account.withdraw(savings_account.get_service_charges())
    investment_account_recent.withdraw(investment_account_recent.get_service_charges())
    investment_account_old.withdraw(investment_account_old.get_service_charges())
except Exception as e:
    print(f"Error updating balances by withdrawing service charges: {e}")
    

# 13. Print each of the bank account objects created in steps 2, 5, 8 and 10.
try:
    print(chequing_account)
    print(savings_account)
    print(investment_account_recent)
    print(investment_account_old)
except Exception as e:
    print(f"Error printing bank accounts: {e}")

