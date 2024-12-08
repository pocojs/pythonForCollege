class BankAccount:
    def __init__(self, number, balance):
        self.account_number = number
        self._balance = balance
                
    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            print("баланс не может быть отрицательным")
        else:
            self._balance = value
            return self._balance
            
    def deposit(self, value):
            self._balance += value
            return self._balance 
            
    def withdraw(self, value):
            self._balance -= value
            return self._balance 
            
account = BankAccount("12345678", 1000) 
account.deposit(500)
account.withdraw(200) 

print(account.balance) 