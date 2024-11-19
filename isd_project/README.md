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


## Assignment 3: Applying Design Patterns - Implemented Strategy and Observer patterns to improve scalability and notification features in the banking system.

### Overview
This project is designed to simulate a banking system that manages multiple account types, including Chequing and Savings accounts, while employing design patterns to enhance its architecture. The primary focus of this implementation is on two key design patterns: the Strategy Pattern and the Observer Pattern.

### Features
- **Account Management**: Users can create and manage different types of bank accounts, including Chequing and Savings accounts, each with specific attributes and functionalities.
- **Service Charge Calculation**: The application calculates service charges based on various strategies implemented for different account types using the Strategy Pattern.
- **Observer Notifications**: Clients are notified of important account events such as low balance warnings or large transactions through the Observer Pattern, enhancing user experience and interaction.

### PART:1
#### Strategy Pattern:
- The Strategy Pattern is employed in this application to encapsulate the algorithms used for calculating service charges for various bank account types. Each account type—ChequingAccount, SavingsAccount, and InvestmentAccount—has its own strategy for charge calculation. This design allows for flexibility and ease of maintenance, as new account types can be added with their own strategies without modifying existing code. The pattern enhances separation of concerns, enabling each strategy to handle its calculation logic independently, leading to cleaner and more manageable code.

### PART:2
#### 2. Observer Pattern:
- The Observer Pattern is utilized to create a notification system where Clients act as observers to BankAccounts (subjects). When significant events occur (like balance changes or large transactions), the accounts notify the clients, providing real-time updates and enhancing user engagement. This design allows for flexible communication between objects, making it easier to extend functionality in the future.

## Event-Driven Programming Paradigm

### Overview

In Assignment 4, the application implements the Event-Driven Programming Paradigm (EDP) to manage user interactions and account transactions. The EDP model is fundamental for creating responsive and interactive applications where the flow of execution is determined by events such as user actions, system messages, or other external factors.

### Key Elements

1. **Signals and Slots**:  
   PySide6’s signal and slot mechanism is used to trigger actions in response to events. In our project, the AccountDetailsWindow emits signals when account transactions (deposit or withdraw) are completed, and these signals are received by the ClientLookupWindow to update the displayed account balance.

2. **Event Handling**:  
   The primary event handlers are connected to widgets, such as buttons, and are responsible for managing user interactions. For example, when a user deposits or withdraws an amount, an event is triggered, updating the balance and ensuring that the GUI is kept in sync with the underlying data.

3. **Signal Emission**:  
   After a successful transaction in the AccountDetailsWindow, a signal is emitted containing the updated BankAccount. This signal notifies other parts of the program (like the ClientLookupWindow) that the data has been changed, allowing the application to update the GUI accordingly.

4. **Signal Reception**:  
   The ClientLookupWindow class listens for the emitted signal and updates the balance in the table for the corresponding account. This ensures that any change made in one window (like a successful transaction) is immediately reflected in the other windows without needing to refresh or manually update the data.

### Benefits of EDP in the Application

- Responsiveness: The application reacts instantly to user actions, ensuring an interactive experience.
- Modularity: Each component of the application (e.g., AccountDetailsWindow, ClientLookupWindow) handles its own specific functionality but communicates through signals, promoting a loosely coupled architecture.
- Real-time Updates: Account balances are updated in real-time across different windows when a transaction is processed.

This event-driven approach helps maintain a fluid user interface and is efficient in handling asynchronous tasks such as transactions and data updates.
