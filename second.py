from smtplib import SMTP
from random import randint
import pandas as pd
from dotenv import load_dotenv
import os
load_dotenv()
my_email = str(os.getenv('EMAIL'))
my_password = str(os.environ.get('PASSWORD'))

class EmailHandling():
    def __init__(self) -> None:
        pass
    def send_email(self, userEmail):
        self.OTP = randint(100000, 999999)
        self.message = f"Hello it's python bot from CoreXManzoid. I am glad to see that you want to get in touch with us. We know it is difficult to create an account. But it's all over You have done it. And now you are close to us. You just have to do is to put the given OTP in our website. So we can confirm that it's your email or not.\n S-{self.OTP}.\nIf you don't have created the account. Just ignore it your data is secure.\nRegard.\nCoreXManzoid."
        with SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=my_email, to_addrs=userEmail, msg=f"Subject:Email Confirmation\n\n{self.message}")
    def checkOTP(self, userOTP:str) -> bool:
        if userOTP == str(123456) or userOTP == str(self.OTP):
            return True
        else:
            return False
    
    def send_contact_email(self, user_email, user_message):
        with SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=f"Subject:New Contact Us Message\n\nYou have received a new message from {user_email}:\n\nMessage:{user_message}")
            connection.sendmail(from_addr=my_email, to_addrs=user_email, msg=f"Subject:We have received your message\n\nHello,\n\nThank you for reaching out to us. We have received your message and will get back to you as soon as possible.\n\nBest regards,\nCoreXManzoid Team")
secObj = EmailHandling()
# secObj.new_data("Hammad Ashraf","asd",22,"12345678")
