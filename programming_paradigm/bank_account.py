class BankAccount:
    """
    A simple BankAccount class to manage basic banking operations.
    """
    def __init__(self, initial_balance=0):
        """
        Initializes the BankAccount with an optional initial balance.
        """
        self.__account_balance = initial_balance  # Encapsulated attribute

    def deposit(self, amount):
        """
        Adds the specified amount to the account balance.
        """
        if amount > 0:
            self.__account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Deducts the specified amount from the account balance if funds are sufficient.
        Returns True if withdrawal is successful, otherwise returns False.
        """
        if amount > 0:
            if amount <= self.__account_balance:
                self.__account_balance -= amount
                return True
            else:
                return False
        else:
            print("Withdrawal amount must be positive.")
            return False

    def display_balance(self):
        """
        Displays the current account balance in a user-friendly format.
        """
        print(f"Current Balance: ${self.__account_balance:.2f}")
