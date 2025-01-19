class BankAccount:
    def __init__(self, initial_balance=0):
        """
        Initialize a bank account with an optional initial balance .
        :param initial_balance: Starting balance  is 0.
        """
        self.account_balance = initial_balance

    def deposit(self, amount):
        """
        Deposit a specified amount into the account.
        :param amount: The amount to deposit (must be positive).
        """
        if amount > 0:
            self.account_balance += amount

    def withdraw(self, amount):
        """
        Withdraw a specified amount from the account.
        :param amount: The amount to withdraw (must be positive).
        :return: True if withdrawal was successful, False if insufficient funds.
        """
        if amount > 0 and self.account_balance >= amount:
            self.account_balance -= amount
            return True
        return False

    def display_balance(self):
        """
        Display the current balance in a user-friendly format.
        """
        print(f"Current Balance: ${self.account_balance:.2f}")
