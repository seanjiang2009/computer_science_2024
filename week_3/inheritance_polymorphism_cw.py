class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start_engine(self):
        print(f"The {self.brand}'s engine starts.")

    def brake(self):
        print(f"The {self.brand} brakes.")
    
class Car(Vehicle):
    def start_engine(self):
        print(f"The {self.brand} car's engine starts with a roar.")
class Motorcycle(Vehicle):
    def start_engine(self):
        print(f"The {self.brand} motorcycle's engine starts with a vroom.")
            
my_car = Car("Toyota")
my_bike = Motorcycle("Honda")

my_car.start_engine() # Outputs: The Toyota car's engine starts with a roar.
my_bike.start_engine() # Outputs: The Honda motorcycle's engine starts with a vroom.

my_car.brake()
my_bike.brake()