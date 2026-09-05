class Vehicle:
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year
    def start(self):
        print("Vehicle is starting")
    def stop(self):
        print("Vehicle has stopped")
class Car(Vehicle):
    def __init__(self,brand,model,year,num_of_doors,num_of_wheels):
        super().__init__(brand,model,year)
        self.num_of_doors = num_of_doors
        self.num_of_wheels = num_of_wheels
class Bike(Vehicle):
    def __init__(self,brand,year,model,num_of_wheels):
        super().__init__(brand,model,year)
        self.num_of_wheels = num_of_wheels
car = Car("Ford","mustang","2005",2,4)
bike = Bike("Hero","2010","Splender","2")
print(car.__dict__)
print(bike.__dict__)
car.start()
bike.stop()

