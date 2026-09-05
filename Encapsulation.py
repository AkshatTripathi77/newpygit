#badbankaccount
class BadBankAccount:
    def __init__(self,balance):
        self.balance = balance
account = BadBankAccount(0.0)
account.balance = -1
print(account.balance)


#GoodBankAccount
class GoodBankAccount:
    def __init__(self):
        self._balance = 0.0
    @property
    def balance(self):
        return self._balance
    def deposit(self,amount):
        if amount <= 0:
            raise ValueError("Deposit value should be greater than Zero")
        self._balance += amount
    def withdraw(self,amount):
        if amount <= 0 :
            raise ValueError("Withdraw amount should be greater than zero")
        if amount >= self._balance:
            raise ValueError("insufficient Funds")
        self._balance -= amount
account = GoodBankAccount()
print(account.balance)
account.deposit(1.99)
print(account.balance)
account.withdraw(1)
print(account.balance)



