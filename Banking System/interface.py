from account import AccountActions, AdvanceAction

def user_interface(account, bank):
    acc_actions = AccountActions(account)
    acc_adv_actions = AdvanceAction(account, bank)
    while True:
        print("\nUser Menu:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Get Transaction History")
        print("5. Take Loan")
        print("6. Transfer Money")
        print("7. Exit")

        choice = input("\n Enter your choice: ")

        if choice == "1":
            amount = int(input("\n Enter amount to deposit: "))
            acc_actions.deposit(amount)
            
        elif choice == "2":
            amount = int(input("\n Enter amount to withdraw: "))
            acc_actions.withdraw(amount)
            
        elif choice == "3":
            print(f"\n Available balance: {acc_actions.check_balance()}")
            
        elif choice == "4":
            print("\n Transaction history: ")
            print("-----------------------")
            for entry in acc_adv_actions.get_transaction_history():
                print(entry)

            
        elif choice == "5":
            amount = int(input("\n Enter loan amount: "))
            acc_adv_actions.take_loan(amount)
            
        elif choice == "6":
            reciver_account_number = int(input("\n Enter reciver account number: "))
            amount = int(input("\n Enter amount to transfer: "))
            acc_adv_actions.transfer(amount, reciver_account_number)
        elif choice == "7":
            break
        
        else:
            print("\n Invalid choice!!, please try again.")
            

def admin_interface(admin):
    while True:
        print("\t\nAdmin Menu:")
        print("1. Create Account")
        print("2. Delete Account")
        print("3. See All Accounts")
        print("4. Check Total Balance")
        print("5. Check Total Loan Amount")
        print("6. Enable/Disable Loan Feature")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            account_type = input("Enter account type (Savings/Current): ").strip().lower()
            admin.create_account(name, email, address, account_type)
            
        elif choice == "2":
            account_number = int(input("\n Enter account number to delete: "))
            admin.delete_account(account_number)
            
        elif choice == "3":
            admin.see_all_accounts()
            
        elif choice == "4":
            admin.check_total_balance()
            
        elif choice == "5":
            admin.check_total_loan_amount()
            
        elif choice == "6":
            enable = input("\n Enable loan feature? (yes/no): ").strip().lower() == "yes"
            admin.toggle_loan_feature(enable)
            
        elif choice == "7":
            break
        
        else:
            print("\n Invalid choice!, Try again!! ")
