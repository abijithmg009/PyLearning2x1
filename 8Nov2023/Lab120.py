#Inheritence. Parent and child
#Father -> Son
#single inhertence: Parent giving to child
#Multilevel = one or more level
# Single inheritence

class Animal:
    def speak(self):
        print("Animal can speak")
    def car(self):
        print("lambo")


class Dog(Animal):

    def speak(self):
        print("Bow Bow")

    def i_want_drive(self):
        Animal().car()


dog = Dog()
dog.speak()
dog.i_want_drive()