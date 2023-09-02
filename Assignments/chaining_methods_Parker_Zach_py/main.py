class User:
    def __init__(self,fname,lname,u_Email,u_Age):
        self.first_name = fname
        self.last_name = lname
        self.full_name = self.first_name + " " + self.last_name
        self.email = u_Email
        self.age = u_Age
        self.is_rewards_member = False
        self.gold_card_pts = 0
        self.monthly_pts_usage = 0
    def enroll_rewards(self):
        if self.is_rewards_member == True:
            print(f"{self.full_name} is already a member")
        else:
            self.is_rewards_member = True
            self.gold_card_pts = 200
            return self
    def spend_points(self,amount):
        if self.gold_card_pts > amount:
            self.gold_card_pts -= amount
            self.monthly_pts_usage += amount
        else:
            print(f"{self.full_name} needs to watch their spending")
        print(f"Thank you for your patronage {self.full_name}")
        print(f"Your new points balance is: {self.gold_card_pts}")
        print(f"Your monthly expenditure of points is: {self.monthly_pts_usage}")
        return self
    def display_u_Info(self):
        print(f"Name:{self.full_name}")
        print(f"Email Address:{self.email}")
        print(f"User Age:{self.age}")
        if self.is_rewards_member == True:
            print("Rewards card has been activated")
        else:
            print("X Rewards card not activated")
        print(f"Current Gold Points:{self.gold_card_pts}")
        print(f"Monthly Points used:{self.monthly_pts_usage}")
        return self
ada_User = User('Ada','Wong','wong@gmail.com',28)
mark_User =User('Mark','Aurelius','mAurel@yahoo.com',37)
brian_User =User('Brian','Badluck','forevercursed@hotmail.com',42)

ada_User.enroll_rewards().spend_points(50).display_u_Info()
mark_User.enroll_rewards().spend_points(80).display_u_Info()
brian_User.enroll_rewards().spend_points(40).display_u_Info()




