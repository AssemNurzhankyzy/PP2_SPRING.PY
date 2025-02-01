class Finance():
    def __init__(self, account, money):
        self.money = money
        self.account = account

    def balance(self):
        return self.money
    
    def owner(self):
        return self.account
    
    def deposit(self, money):
        self.money+=money

        return f"You have {money} money in your deposit"
    
    def withdraw(self, money):
        if self.money - money < 0:
            return "Insufficient money on your account"
        else:
            self.money-=money

            return f"You have {self.money} in your account,  and you are taking  {money}"
        
        
bank = Finance("Assem", 100)
print(bank.balance())
print(bank.owner())
print(bank.deposit(100000))
print(bank.withdraw(42500))
print(bank.withdraw(650))
print(bank.withdraw(99999999))
print(bank.withdraw(0))