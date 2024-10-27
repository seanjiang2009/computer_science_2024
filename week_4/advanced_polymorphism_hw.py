class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(f"{self.name} makes a sound.")

class Cat(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
    def speak(self):
        super().speak()
        print(f"{self.name}, the {self.breed} cat meows.")

class Dog(Animal):
    def speak(self):
        super().speak()
        print(f"{self.name} barks.")

class Owl(Animal):
    def speak(self):
        super().speak()
        print(f"{self.name} hoots.")

def speak(any_animal):
    any_animal.speak()

hermiones_cat = Cat("Crookshanks", "Orange")
hagrids_dog = Dog("Fang")
harrys_owl = Owl("Hedwig")

hermiones_cat.speak()
hagrids_dog.speak()
harrys_owl.speak()

speak(hermiones_cat)
speak(hagrids_dog)
speak(harrys_owl)



#Add a Cat class that inherits from Animal and overrides
#the speak() method.
#Use super() to call the parent class’s speak() method first.
#Demonstrate polymorphism by creating a list of
#Dog , Bird , and Cat objects and passing
#them to a function that calls speak() on each.