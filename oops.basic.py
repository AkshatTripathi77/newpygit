class Dog:
    def __init__(self,name,breed,owner):
        self.name = name
        self.breed = breed
        self.owner = owner
    def bark(self):
        print("Whoof whoof")
class Owner:
    def __init__(self,name,address,contact_Num):
        self.name = name
        self.address = address
        self.PhoneNum = contact_Num
owner1 = Owner("Downey",'122Delhi',"1234567")
dog1 = Dog("Bruce",'Scottish', owner1)
owner2 = Owner("hella","698Mumbai","981627482")
dog2 = Dog("Freya","Indian", owner2)
print(dog1.owner.PhoneNum)
print(dog1.name)
print(dog2.breed)
