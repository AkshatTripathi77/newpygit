class User:
    def __init__(self,username,email,password):
        self.username = username
        self._email = email
        self.password = password
    @property
    def email(self):
        return self._email
    @email.setter
    def email(self,new_email):
        if "@" in new_email:
            self._email= new_email
user1 = User("Akshat","akshat@gmail.com","789456123")
print(user1.email)
user1.email = "Ananyagmail.com"
print(user1.email)

