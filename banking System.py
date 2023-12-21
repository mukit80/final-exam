import random

# User Class
class User:
    def __init__(self, name, email, address, account_type):
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.balance = 0
        self.account_number = random.randint(10000, 99999)
        self.loan_limit = 2
        self.loan_count = 0
        self.transactions = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Deposited ${amount}")
        else:
            print("Invalid amount for deposit.")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                self.transactions.append(f"Withdrew ${amount}")
            else:
                print("Withdrawal amount exceeded.")
        else:
            print("Invalid amount for withdrawal.")

    def check_balance(self):
        return self.balance

    def view_transaction_history(self):
        for transaction in self.transactions:
            print(transaction)

    def take_loan(self, amount):
        if self.loan_count < self.loan_limit:
            self.balance += amount
            self.loan_count += 1
            self.transactions.append(f"Loan of ${amount} taken.")
        else:
            print("You have reached the maximum limit for loans.")

    def transfer_funds(self, recipient, amount):
        if recipient is not None:
            if self.balance >= amount:
                self.balance -= amount
                recipient.balance += amount
                self.transactions.append(f"Transferred ${amount} to account {recipient.account_number}")
            else:
                print("Insufficient funds for the transfer.")
        else:
            print("Recipient account does not exist.")

# Admin Class
class Admin:
    def __init__(self):
        self.users = []

    def create_user_account(self, name, email, address, account_type):
        user = User(name, email, address, account_type)
        self.users.append(user)
        return user

    def delete_user_account(self, user):
        if user in self.users:
            self.users.remove(user)
            print("User account deleted.")
        else:
            print("User account not found.")

    def list_all_user_accounts(self):
        for user in self.users:
            print(f"Account Number: {user.account_number}, Name: {user.name}, Email: {user.email}, Account Type: {user.account_type}")

    def check_bank_balance(self):
        total_balance = sum(user.check_balance() for user in self.users)
        return total_balance

    def check_loan_amount(self):
        total_loan = sum(user.check_balance() for user in self.users)
        return total_loan

    def toggle_loan_feature(self, enable):
        for user in self.users:
            user.loan_limit = 2 if enable else 0

# Main Program
admin = Admin()

while True:
    print("\nPress 1 to Create an account")
    print("Press 2 to Log in as user")
    print("Press 3 to Log in as admin")
    print("Press 4 to Exit")

    choice = input("Enter your option: ")

    if choice == "1":
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        address = input("Enter your address: ")
        account_type = input("Enter account type (Savings/Current): ")

        user = admin.create_user_account(name, email, address, account_type)
        print(f"Account created successfully. Your account number is {user.account_number}")

    elif choice == "2":
        account_number = int(input("Enter your account number: "))
        user = None
        for u in admin.users:
            if u.account_number == account_number:
                user = u
                break

        if user:
            print(f"Welcome, {user.name}!")
            while True:
                print("\nPress 1 to Deposit Money")
                print("Press 2 to Withdraw Money")
                print("Press 3 to Check Balance")
                print("Press 4 to View Transaction History")
                print("Press 5 to Take a Loan")
                print("Press 6 to Transfer Money")
                print("Press 7 to Exit User Menu")

                user_choice = input("Enter your option: ")

                if user_choice == "1":
                    amount = float(input("Enter the amount to deposit: "))
                    user.deposit(amount)

                elif user_choice == "2":
                    amount = float(input("Enter the amount to withdraw: "))
                    user.withdraw(amount)

                elif user_choice == "3":
                    print(f"Your current balance is ${user.check_balance()}")

                elif user_choice == "4":
                    user.view_transaction_history()

                elif user_choice == "5":
                    amount = float(input("Enter the loan amount: "))
                    user.take_loan(amount)

                elif user_choice == "6":
                    recipient_account = int(input("Enter recipient's account number: "))
                    recipient = None
                    for u in admin.users:
                        if u.account_number == recipient_account:
                            recipient = u
                            break

                    if recipient:
                        amount = float(input("Enter the amount to transfer: "))
                        user.transfer_funds(recipient, amount)
                    else:
                        print("Recipient account does not exist.")

                elif user_choice == "7":
                    break

        else:
            print("Account not found. Please check your account number.")

    elif choice == "3":
        admin_password = "admin123"  # Change this to a more secure password
        password = input("Enter admin password: ")

        if password == admin_password:
            while True:
                print("\nPress 1 to Delete a User Account")
                print("Press 2 to List All User Accounts")
                print("Press 3 to Check Bank Balance")
                print("Press 4 to Check Loan Amount")
                print("Press 5 to Toggle Loan Feature")
                print("Press 6 to Exit Admin Menu")

                admin_choice = input("Enter your option: ")

                if admin_choice == "1":
                    account_number = int(input("Enter the account number to delete: "))
                    user_to_delete = None
                    for u in admin.users:
                        if u.account_number == account_number:
                            user_to_delete = u
                            break

                    if user_to_delete:
                        admin.delete_user_account(user_to_delete)
                    else:
                        print("Account not found. Please check the account number.")

                elif admin_choice == "2":
                    admin.list_all_user_accounts()

                elif admin_choice == "3":
                    print(f"Bank's total balance is ${admin.check_bank_balance()}")

                elif admin_choice == "4":
                    print(f"Total loan amount is ${admin.check_loan_amount()}")

                elif admin_choice == "5":
                    enable_loans = input("Do you want to enable loans? (yes/no): ")
                    admin.toggle_loan_feature(enable_loans.lower() == "yes")

                elif admin_choice == "6":
                    break

        else:
            print("Admin password incorrect. Please try again.")

    elif choice == "4":
        print("Exiting the system.")
        break
