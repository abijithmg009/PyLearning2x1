# Overriding - same name function for parent and child
#child can always override the parent functionality
#super() means call my parent function


class Animal:
    def sound(self):
        print("Animal sound")

class Dog(Animal):
    pass
    def sound(self):
        super().sound()
        print("Dog Sound")


#animal = Animal()
#animal.sound()
dog = Dog()
dog.sound()
