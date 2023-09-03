class BankAccount:
    def __init__(self,user_name,user_email,user_bal):
        self.user_name = user_name
        self.user_email = user_email
        self.user_bal = user_bal
    def deposit(self,amount):
        self.user_bal += amount
        print(f"{self.user_name} thank you for your deposit")
        return self
    def withdraw(self,amount):
        if self.user_bal > amount:
            self.user_bal -= amount
            print(f"{self.user_name} your withdrawal has been successful")
            print(f"have a wonderful day {self.user_name} !")
        else:
            print(f"{self.user_name} you have insufficient funds!")
            input(f"{self.user_name} please enter the amount you wish to withdraw")
        return self
    def bank_status(self):
        print(f"{self.user_name} your current balance is: $ {self.user_bal}")
        return self
    def yield_interest(self):
        if self.user_bal > 0:
            self.user_bal *= (1.00 + 0.04)
        self.user_bal = round(self.user_bal,3)
        return self
# user1 = BankAccount('Connor Ferris','connerF@gmail.com',100.00)
# user2 = BankAccount('Matt Broderick','mattB@yahoo.com',150.00)
# user1.deposit(50).deposit(40).deposit(2).withdraw(100).yield_interest().bank_status()
# user2.deposit(10).deposit(100).withdraw(100).withdraw(10).withdraw(50).withdraw(27).yield_interest().bank_status()
class User:
    def __init__(self,name,email,bal):
        self.account = BankAccount(user_name=name,user_email=email,user_bal=bal)
        self.name = name
        self.email = email
        self._transaction = bal
    def make_deposit(self,amount):
        self.account.deposit(amount)
        return self
    def make_withdraw(self,amount):
        self.account.withdraw(amount)
        return self
    def u_Balance(self):
        print(f"your bank balance is: ${self.account.user_bal}.00")
        return self
user1 = User('Joseph Merdon','Farquad@aol.com',300)
user2 = User('Freddy Needlemire','runningdownmid@gmail.com',500)
user1.make_deposit(50).make_withdraw(100).u_Balance()




