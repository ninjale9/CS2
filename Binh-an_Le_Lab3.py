class BankAccount: 
    def __init__(self,new_name,checking_balance,savings_balance) :
        self.new_name = new_name
        self.checking_balance = checking_balance
        self.savings_balance = savings_balance

    def deposit_checking (self,amount,) :
        self.checking_balance += amount

    def deposit_savings (self,amount) :
        self.savings_balance += amount 

    def withdraw_checkings (self,amount) : 
        if amount > self.checking_balance:
            print("Sorry, You do not have enough funds in your checking savings. ")
        else :
            self.checking_balance -= amount

    def withdraw_savings (self,amount) :
        if amount > self.savings_balance :
            print("Sorry you do not have enough funds in your savings to windraw.")
        else : 
            self.savings_balance -= amount 

    def transfer_to_savings (self,amount):
        if amount > self.checking_balance :
            print("You do not have enough money to transfer to your savings. ")
        else : 
            self.checking_balance -= amount 
            self.savings_balance += amount

account = BankAccount("Mickey", 500.00, 1000.00)    
account.checking_balance = 500    
account.savings_balance = 500    
account.withdraw_savings(100)    
account.withdraw_checkings(100)    
account.transfer_to_savings(300)    
print(account.new_name)    
print(f'${account.checking_balance:.2f}')    
print(f'${account.savings_balance:.2f}')
