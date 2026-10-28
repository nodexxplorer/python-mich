class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance 
        
acc = BankAccount("Michael", 20000)
acc.balance = -99999

print(acc.balance)