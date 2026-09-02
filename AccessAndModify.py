from datetime import datetime
class User:
    def __init__(self,username,email,password):
        self.username = username
        self._email = email
        self.password = password
    def clean_email(self):
        return self._email.lower().strip()

    def get_mail(self):
        print(f"Email accessed at {datetime.now()}")
        return self._email
    def set_email(self,new_email):
        if "@" in new_email:
            self._email = new_email
        else:
            print("Enter a valid Email")

user1 = User("Akshat","pubg@gmail.com","123456789")
print(user1.get_mail())
user1.set_email("bgmi@gmail.com")
print(user1.get_mail())
