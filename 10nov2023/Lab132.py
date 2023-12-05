#Abstraction - OOPs
#Hiding the important details and showing the what is required

#car -> start engine -> Put the Gear -> Start driving
#Do you know how the car was started, gear was manufactured
# we hide the core implementation and show only important details

# to represent the complex systems by simplifying and hiding unnecessary details
#ABC - Abstract Base Class
# Abstract Base Method
"""
Shape = Rectangle, Circle
Shape = Perimeter, Area
"""

"""
Animal(speak) = Dog, Cat, Cow, Tiger

"""
from abc import ABC,abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Bow Bow"

class Cat(Animal):
    def sound(self):
        return "Meow Meow"

class Tiger(Animal):
    def sound(self):
        return "Roar Roar"

#Who ever inhertited from Animal, they need to complete the sound function

dog = Dog()
print(dog.sound())
cat = Cat()
print(cat.sound())
tiger = Tiger()
print(tiger.sound()) # will show error if it didn't complete the sound function.

#animal = Animal()