class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def greet(self):
        print(f"Hello my name is {self.name} and my age is {self.age}")
person1 = Person("Akshat",20)
person1.greet()
person2 = Person("Ananya",14)
person2.greet()

