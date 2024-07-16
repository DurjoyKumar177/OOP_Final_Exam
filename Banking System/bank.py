from account import Account
class Bank:
    def __init__(self):
        self.accounts = {}
        self.total_loan_amount = 0
        self.loan_feature_enabled = True

    def create_account(self, name, email, address, account_type):
        if account_type not in ["savings", "current"]:
            print("\n Invalid account type. Please choose 'Savings' or 'Current'.")
            return None

        new_account = Account(name, email, address, account_type)
        self.accounts[new_account.account_number] = new_account
        print(f"\n \n Account created successfully!!. \n\tAccount Number: {new_account.account_number}\n")
        return new_account

    def find_account(self, account_number):
        return self.accounts.get(account_number, None)

    def delete_account(self, account_number):
        if account_number in self.accounts:
            del self.accounts[account_number]
            print(f"\n Account {account_number} deleted successfully.!!")
        else:
            print("\n Account not found.!!")

    def get_all_accounts(self):
        return self.accounts.values()

    def get_total_balance(self):
        return sum(account.balance for account in self.accounts.values())

    def toggle_loan_feature(self, enable):
        self.loan_feature_enabled = enable

        if enable:
            status = "enabled"
        else:
            status = "disabled"
        
        print(f"\n Loan feature has been {status}.")
