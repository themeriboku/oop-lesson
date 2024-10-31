class Account:
    def __init__(self, num, type, account_name, balance):
        self.account_number = num
        self.type = type
        self.account_name = account_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount

    def __str__(self):
        return '{' + str(self.account_number) + ',' + str(self.type) + ',' + str(self.account_name) + ',' + str(self.balance) + '}'


account1 = Account("0000", "saving", "David Patterson", 1000)
account2 = Account("0001", "checking", "John Hennessy", 2000)
account3 = Account("0003", "saving", "Mark Hill", 3000)
account4 = Account("0004", "saving", "David Wood", 4000)
account5 = Account("0004", "saving", "David Wood", 4000)
print(account1)
account1.deposit(1000)
account2.withdraw(200)
print(account2)
print(account3)
print(account4)
print(account5)
