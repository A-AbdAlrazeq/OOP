class User:
    def __init__(self, name, account_balance):
        self.name = name
        self.account_balance = account_balance

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print("User:", self.name, "Balance:", self.account_balance)
        return self

    def transfer_money(self, other_user, amount):
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)


Abd = User("Abd", 300)
ahmad = User("ahmad", 500)
john = User("john", 250)

Abd.make_deposit(50).make_deposit(80).make_deposit(
    120).make_withdrawal(300).display_user_balance()

ahmad.make_deposit(50).make_deposit(80).make_withdrawal(
    120).make_withdrawal(300).display_user_balance()

john.make_deposit(50).make_withdrawal(80).make_withdrawal(
    120).make_withdrawal(300).display_user_balance()

Abd.transfer_money(john, 300)
print("_"*40)
Abd.display_user_balance()
john.display_user_balance()
