#Constructor - way to initilize object.
#Inheritence -
#Encapsulation - Attributes + Method
#Polymorphism -
#Absctraction

#Constructor
"""
help to initilize the object attribute
__init__() this method
"""
a = 10 # this is global variable which can be initilized outside class
class Car:
    name = "Abijith" #class variable where the variable is available for both functions.

    def __init__(self, make, model): #default constructor
        self.make = make #instance variable
        self.model = model #instance variable
        print("I will be called first "+ self.name)


    def start_engine(self):
        print("Starting the car", self.make, self.model)

car1 = Car("Toyota", "Camere")
car2 = Car("Honda", "Civic")
car1.start_engine()
car2.start_engine()
# the moment we create object, a special function is called automatically __init__()
# All the attributes can be initilize and add some initial value to them

print(id(car1))
print(id(car2))