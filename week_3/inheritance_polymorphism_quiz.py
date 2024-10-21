class Vehicle:
    def __init__(self, name):
        self.name = name
    def start_engine(self):
        print("the engine starts.")

class Car(Vehicle):
    def start_engine(self):
        print("the car's engine starts.")

class Motorcycle(Vehicle):
    def start_engine(self):
        print("the motorcycle's engine starts.")

def start_engine(one_vehicle):
    one_vehicle.start_engine()
    #print("the engine starts.")

seans_car = Car("Sean's Car")
seans_motorcycle = Motorcycle("Sean's Motorcycle")

seans_car.start_engine()
seans_motorcycle.start_engine()

start_engine(seans_car)
start_engine(seans_motorcycle)