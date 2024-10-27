class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(f"{self.name} makes a sound.")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name) # Calls the parent class's __init__ method
        self.breed = breed
    def speak(self):
        super().speak() # Calls the parent class's speak method
        print(f"{self.name} barks.")

# Create a Dog object
my_dog = Dog("Rex", "Golden Retriever")
my_dog.speak()