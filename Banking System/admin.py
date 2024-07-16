class Admin:
    def __init__(self, bank):
        self.bank = bank

    def create_account(self, name, email, address, account_type):
        return self.bank.create_account(name, email, address, account_type)

    def delete_account(self, account_number):
        self.bank.delete_account(account_number)

    def see_all_accounts(self):
        accounts = self.bank.get_all_accounts()
        for account in accounts:
            print(f"\n Account Number: {account.account_number}, Name: {account.name}, Balance: {account.balance}")

    def check_total_balance(self):
        total_balance = self.bank.get_total_balance()
        print(f"\n Total available balance in the bank: {total_balance}")

    def check_total_loan_amount(self):
        total_loan = self.bank.total_loan_amount
        print(f"\n Total loan amount: {total_loan}")

    def toggle_loan_feature(self, enable):
        self.bank.toggle_loan_feature(enable)
