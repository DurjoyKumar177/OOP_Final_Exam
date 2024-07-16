from bank import Bank
from admin import Admin
from interface import user_interface, admin_interface

bank = Bank()
admin = Admin(bank)

while True:
    print("\n Main Menu:")
    print("1. Admin")
    print("2. User")
    print("3. Exit")

    role = input("\n Enter your role (Admin/User): ").strip().lower()

    if role == "admin" or role == "1":
        admin_interface(admin)
            
    elif role == "user" or role == "2":
        print("1. Already have Account. ")
        print("2. Creat Account.")
        choice = input( "\n Enter your Selection: ")
        if choice == "1":
            account_number = int(input("\n Enter your account number: "))
            account = bank.find_account(account_number)
            if account:
                user_interface(account, bank)
                    
            else:
                print("\n Account not found.")
            
        elif choice == "2":
            name = input("Enter name: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            account_type = input("Enter account type (Savings/Current): ").strip().lower()
            admin.create_account(name, email, address, account_type)
                
        else:
            print("\n Invalid role, please try again.")
                
    elif role == "exit" or role == "3":
        break
        
    else:
        print("\n Invalid role, please try again.")    


