class Appliance:
    def __init__(self, name):
        self.name = name
    def turn_on(self):
        print("The appliance is now on")

class WashingMachine(Appliance):
    def turn_on(self):
        print("The washing machine is now running")

class Refrigerator(Appliance):
    def turn_on(self):
        print("The refrigerator is now cooling")

def turn_on(any_appliance):
    any_appliance.turn_on()

seans_washingmachine = WashingMachine("Sean's Washing Machine")
seans_refrigerator = Refrigerator("Sean's Refrigerator")

turn_on(seans_washingmachine)
turn_on(seans_refrigerator)