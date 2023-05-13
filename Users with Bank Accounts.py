class BankAccount:
    def __init__(self, int_rate=0, balance=0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdrawal(self, amount):
        if amount > self.balance:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
            return self
        else:
            self.balance -= amount
            return self

    def display_account_info(self):
        print("Balance:", "$"+str(self.balance))
        return self


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.accounts = {
            "checking": BankAccount(int_rate=0.01, balance=0),
            "savings": BankAccount(int_rate=0.03, balance=0)
        }

    def make_deposit(self, amount, account):
        self.accounts[account].deposit(amount)

    def make_withdrawal(self, amount, account):
        self.accounts[account].withdrawal(amount)

    def display_user_balance(self, account):
        print("User:", self.name, ",Account name:", account, ",Balance:", "$" +
              str(self.accounts[account].balance))


Abd = User("Abd", "abood@gmail.com")
Abd.make_deposit(300, "checking")
Abd.make_withdrawal(150, 'checking')
Abd.make_withdrawal(100, 'checking')
Abd.display_user_balance("checking")

Abd.make_deposit(400, "savings")
Abd.make_deposit(100, 'savings')
Abd.make_withdrawal(100, 'savings')
Abd.make_withdrawal(250, 'savings')
Abd.display_user_balance("savings")
