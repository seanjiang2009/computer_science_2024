#parent class
class Appliance:
    def __init__(self, name):
        self.name = name

    def turn_on(self):
        print(f"{self.name} is running.")

#child class
class Washing_Machine(Appliance):
    def turn_on(self):
        print(f"{self.name} is washing.")

class Refrigerator(Appliance):
    def turn_on(self):
        print(f"{self.name} is freezing.")

def turn_on_any_appliance(Appliance):
    Appliance.turn_on()

sean_washing_machine = Washing_Machine("Sean's washing machine")
sean_washing_machine.turn_on()

sean_refrigerator = Refrigerator("Sean's refrigerator")
sean_refrigerator.turn_on()

turn_on_any_appliance(sean_washing_machine)
turn_on_any_appliance(sean_refrigerator)

#Challenges: understanding and implementing polymorphism, correct grammar when creating child classes.
#Method overriding helped customize the behavior of the child classes by being able to
# specifically edit the wording in the methods without entirely changing the method.