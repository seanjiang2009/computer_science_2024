class Animal:
    def speak(self):
        print("The animal makes a sound.")

class Dog(Animal):
    def speak(self):
        print("The dog barks.")

def make_animal_speak(animal):
    animal.speak()

my_dog = Dog()
my_dog.speak() # Outputs: The dog barks.
make_animal_speak(my_dog) # Outputs: The dog barks.

