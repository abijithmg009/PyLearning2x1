#Hirarchel

class Vehicle:
    def info(self):
        return "This is a vehicle"
class Car(Vehicle):
    def info(self):
        return "This is a car"
class bycycle(Vehicle):
    def info(self):
        return "This is a bycycle"

car = Car()
bycycle = bycycle()
print(car.info())
print(bycycle.info())