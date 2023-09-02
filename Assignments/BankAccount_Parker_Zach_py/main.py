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
            print(f"{self.user_name} your withdrawel has been successful")
            print(f"have a wonderful day {self.user_name}")
        else:
            print(f"{self.user_name} you have insufficient funds!")
            input(f"{self.user_name} please enter the amount you wish to withdraw")
        return self
    def bank_status(self):
        print(f"{self.user_name} your current balance is: $ {self.user_bal}")
        return self
    def yield_interest(self):
        print(self.user_bal)
        if self.user_bal < 0:
            self.user_bal = self.user_bal * (1 + 0.04)
        print(self.user_bal)
        return self
user1 = BankAccount('Connor Ferris','connerF@gmail.com',100)
user2 = BankAccount('Matt Broderick','mattB@yahoo.com',150)
user1.deposit(50).deposit(40).deposit(2).withdraw(100).yield_interest().bank_status()
user2.deposit(10).deposit(100).withdraw(100).withdraw(10).withdraw(50).withdraw(27).yield_interest().bank_status()
