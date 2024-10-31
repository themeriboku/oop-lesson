class AccountDB:
    def __init__(self):
        self.account_database = []

    def insert(self, account):
        index = self.__search_private(account.account_number)
        if index == -1:
            self.account_database.append(account)
        else:
            print(account, "Duplicated account; nothing to be insert")
    
    def __search_private(self, account_num):
        for i in range(len(self.account_database)):
            if self.account_database[i].account_number == account_num:
                return i
        return -1
    
    def search_public(self, account_num):
        for account in self.account_database:
            if account.account_number == account_num:
                return account
        return None
    
    def delete(self, account_num):
        index = self.__search_private(account_num)
        if index != -1:
            del self.account_database[index]
            return True
        return False
    
    def __str__(self):
        s = ''
        for account in self.account_database:
            s += str(account) + ", "
        return s

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


def test_delete_method():   
    account_db = AccountDB()
    
    account1 = Account(101, "Saving", "Alice", 1000)
    account2 = Account(102, "Checking", "Bob", 1500)
    account3 = Account(103, "Saving", "Charlie", 2000)
    
    account_db.insert(account1)
    account_db.insert(account2)
    account_db.insert(account3)
    
    print("Initial database:")
    print(account_db)

    success = account_db.delete(102)
    if success:
        print("Account 102 deleted successfully.")
    else:
        print("Account 102 not found.")
    
    print("Database after deleting account 102:")
    print(account_db)

    success = account_db.delete(999)
    if success:
        print("Account 999 deleted successfully.")
    else:
        print("Account 999 not found.")
    
    print("Final database:")
    print(account_db)

test_delete_method()