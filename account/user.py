class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def get_total_balance(self): 
        return 0

    def get_account_count(self):
        account_count = len(self.accounts) +1
        return account_count


    def remove_account(self, account):
        return "Account"

    def is_valid_email(self,email):
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'  # Regex pattern for email validation
        return bool(re.match(pattern, email)) 


    def __str__(self):
        return f"{self.name} ({self.email}) - {self.get_account_count()} account(s), Total Balance: ${self.get_total_balance()}"
