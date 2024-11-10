class Person:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def speak(self):
        print(f"Hello.")

class Student(Person):
    def __init__(self, name, gender, GPA):
        super().__init__(name, gender)
        self.GPA = GPA

    def speak(self):
        print(f"Hello! My name is {self.name}. How are you?")

class Teacher(Person):
    def __init__(self, name, gender, subject):
        super().__init__(name, gender)
        self.subject = subject

    def speak(self):
        print(f"Hey there, my name is {self.name} and I teach {self.subject}.")
    
def make_person_speak(any_person):
    any_person.speak

MrGuy = Teacher("Mr. Guy", "male", "English")
William = Student("William", "male", "4.0")

make_person_speak(MrGuy)
make_person_speak(William)