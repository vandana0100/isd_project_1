# Intermediate Software Development Automated Teller Project
This project will be developed over the course of several assignments.  Each 
assignment will build on the work done in the previous assignment(s).  Ultimately, 
an entire system will be created to manage bank transactions for clients who 
have one or more bank accounts.

## Author
Vandana Bhangu

## Assignment
Assignment 1: Classes, Encapsulation and Unit Test Planning 
The assignment focuses on creating classes that protect their data using encapsulation. We'll also plan and write tests to make sure your classes and methods work correctly.

## Encapsulation
In the BankAccount and Transaction classes, encapsulation was used by keeping important details like the account balance and transaction amount private. This means other parts of the program can’t change them directly and can only access or update them through special methods, making the data more secure.

## Assignment 2:
Assignment 2: Abstraction, Inheritance and Polymorphism.
In this assignment, I will extend the previous bank account project by creating separate classes for Chequing, Investment, and Savings accounts. I will also write corresponding unit tests for each account type.

## Polymorphism
Polymorphism in this project allows different types of bank accounts to use the same methods but behave differently based on their type. The BankAccount class defines general methods like deposit(), withdraw(), and get_service_charges(). Each subclass—ChequingAccount, SavingsAccount, and InvestmentAccount—overrides the get_service_charges() method to calculate fees specific to that account type.

ChequingAccount: Charges based on overdraft.
SavingsAccount: Charges if the balance falls below a minimum.
InvestmentAccount: Charges based on how long the account has been open.
This allows the program to treat all accounts the same way while letting each account handle its specific rules for service charges.