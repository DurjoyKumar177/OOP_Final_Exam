import random

class Account:
    def __init__(self, name, email, address, account_type):
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.balance = 0
        self.account_number = self.generate_account_number()
        self.transaction_history = []
        self.loan_count = 0

    def generate_account_number(self):
        return random.randint(1000000000, 9999999999)

class AccountActions:
    def __init__(self, account):
        self.account = account

    def deposit(self, amount):
        self.account.balance += amount
        self.account.transaction_history.append(f"Deposited: {amount}")
        print(f"\n Deposited {amount} to account {self.account.account_number}")

    def withdraw(self, amount):
        if amount > self.account.balance:
            print("\n Withdrawal amount exceeded")
            
        else:
            self.account.balance -= amount
            self.account.transaction_history.append(f"Withdrawn: {amount}")
            print(f"\n Withdrawn {amount} from account {self.account.account_number}")

    def check_balance(self):
        return self.account.balance

class AdvanceAction:
    def __init__(self, account, bank):
        self.account = account
        self.bank = bank

    def get_transaction_history(self):
        return self.account.transaction_history

    def take_loan(self, amount):
        if not self.bank.loan_feature_enabled:
            print("\n Loan feature is currently disabled.")
            return

        if self.account.loan_count < 2:
            self.account.balance += amount
            self.account.loan_count += 1
            self.account.transaction_history.append(f"Loan taken: {amount}")
            self.bank.total_loan_amount += amount
            print(f"\n Loan of {amount} taken. Current balance: {self.account.balance}")
            
        else:
            print("\n Loan limit exceeded")

    def transfer(self, amount, reciver_account_number):
        reciver_account = self.bank.find_account(reciver_account_number)
        if not reciver_account:
            print("\n Account does not exist")
            
        elif amount > self.account.balance:
            print("\n Withdrawal amount exceeded")
            
        else:
            self.account.balance -= amount
            reciver_account.balance += amount
            self.account.transaction_history.append(f"\n Transferred: {amount} to account {reciver_account.account_number}")
            reciver_account.transaction_history.append(f"\n Received: {amount} from account {self.account.account_number}")
            print(f"\n Transferred {amount} to account {reciver_account.account_number}")