# bank_account.py

class Account:
    def __init__(self, account_number, holder_name, initial_balance=0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount:.2f} to account {self.account_number}.")

    def withdraw(self, amount):
            self.balance -= amount
            print(f"Withdrew (amount:.2f} from account {self.account_number}.")

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"Account {self.account_number} Holder: {self.holder_name} Balance: {self.balance:.2f}"


class SavingsAccount(Account):
    def __init__(self, account_number, holder_name, interest_rate, initial_balance=0):
        super().__init__(account_number, holder_name, initial_balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * (self.interest_rate / 100)
        self.balance += interest
        print(f"Interest of {interest:.2f} added to account {self.account_number}.")

    def __str__(self):
        return (f"Savings Account {self.account_number} Holder: {self.holder_name} "
                f"Balance: {self.balance:.2f} Interest Rate: {self.interest_rate:.1f}")


class CheckingAccount(Account):
    def __init__(self, account_number, holder_name, overdraft_limit, initial_balance=0):
        super().__init__(account_number, holder_name, initial_balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        if amount > self.balance + self.overdraft_limit:
            print("Withdrawal exceeds overdraft limit.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount:.2f} from account {self.account_number}.")

    def __str__(self):
        return (f"Checking Account {self.account_number} Holder: {self.holder_name} "
                f"Balance: {self.balance:.2f} Overdraft Limit: {self.overdraft_limit:.2f}")


