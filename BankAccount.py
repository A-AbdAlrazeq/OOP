
class BankAccount:
    def __init__(self, int_rate=0.01, balance=0):
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

    def yield_interest(self):
        self.balance += self.balance*self.int_rate
        return self


Abd = BankAccount()
Ahmad = BankAccount()
Abd.deposit(200).deposit(300).deposit(100).withdrawal(
    500).yield_interest().display_account_info()

Ahmad.deposit(100).deposit(200).withdrawal(200).withdrawal(100).withdrawal(
    50).withdrawal(100).yield_interest().display_account_info()
