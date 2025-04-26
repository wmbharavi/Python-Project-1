from account.user import User
from account.bank_account import BankAccount, SavingsAccount, CurrentAccount, StudentAccount

users = []

def create_user():
    name = input("Enter name: ").strip()  # Removes leading/trailing spaces
    email = input("Enter email: ").strip()
    user = User(name, email)
    
    if not user.is_valid_email(email):  # Check if the email is NOT valid
        print(f"Email '{email}' is invalid! Please enter a valid email address.")
    else:
        users.append(user)
        print(f"User {name} created successfully.\n")



def list_users():
    if not users:  # Check if users list is empty
        print("No users found! Please add a user first.")
        return
        
    for i, user in enumerate(users):
        print(f"{i+1}. {user}")

def create_account():
    if not users:  # Check if users list is empty
        print("No users found! Please add a user first.")
        return

    list_users()
    idx = int(input("Select user number: ")) - 1

    if idx < 0 or idx >= len(users):  # Ensure the selected index is valid
        print("Invalid user selection!")
        return

    print("Account Type:")
    print("1. Savings Account")
    print("2. Students Account")
    print("3. Current Account")
    account_choice = int(input("Enter your choice (1, 2, 3): "))
    amount = float(input("Enter initial deposit: "))

    if account_choice == 1:
        account = SavingsAccount(amount)
    elif account_choice == 2:
        account = StudentAccount(amount)
    elif account_choice == 3:
        account = CurrentAccount(amount)
    else:
        print("Invalid choice!")
        account = BankAccount(amount)

    users[idx].add_account(account)
    print(f"{account.get_account_type()} added!\n")

def deposit_money():
    if not users:  # Ensure there are users
        print("No users found! Please add a user first.")
        return

    list_users()
    idx = int(input("Select user: ")) - 1

    if idx < 0 or idx >= len(users):  # Validate user index
        print("Invalid user selection!")
        return

    user = users[idx]

    if not user.accounts:  # Ensure the user has accounts
        print(f"User {user.name} has no accounts! Please create one first.")
        return

    for i, acc in enumerate(user.accounts):
        print(f"{i+1}. Balance: Rs. {acc.get_balance()}")

    acc_idx = int(input("Select account: ")) - 1

    if acc_idx < 0 or acc_idx >= len(user.accounts):  # Validate account index
        print("Invalid account selection!")
        return

    amount = float(input("Enter amount to deposit: "))

    if amount <= 0:  # Ensure deposit amount is valid
        print("Deposit amount must be positive!")
        return

    user.accounts[acc_idx].deposit(amount)
    print(f"Rs. {amount} deposited successfully into account {acc_idx+1}. New balance: Rs. {user.accounts[acc_idx].get_balance()}")


def withdraw_money():
    list_users()
    idx = int(input("Select user: ")) - 1
    user = users[idx]
    for i, acc in enumerate(user.accounts):
        print(f"{i+1}. Balance: Rs. {acc.get_balance()}")
    acc_idx = int(input("Select account: ")) - 1
    amount = float(input("Enter amount to withdraw: "))
    try:
        user.accounts[acc_idx].withdraw(amount)
        print("Withdrawal successful.\n")
    except ValueError as e:
        print(f"Error: {e}\n")

def view_transactions():
    list_users()
    idx = int(input("Select user: ")) - 1
    if not users:  # Check if users list is empty
        print("\n No users found! Please add a user first.")
        return
    elif users[idx]:
    for i, acc in enumerate(user.accounts):
        print(f"\n{acc.get_account_type()} {i+1} - Balance: Rs. {acc.get_balance()}")
        for tx in acc.get_transaction_history():
            print(tx)

