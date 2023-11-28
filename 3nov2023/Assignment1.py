#Create a Car class and Create 2 Objects of the class with attributes 5 and 5 methods


class Car:
    name = None
    color = None
    model = None
    top_speed = None
    company = None

    def car_start(self):
        print(f"{self.name} is started")

    def car_running(self):
        print(f"The {self.color} car is running good")

    def car_speed(self):
        print(f"{self.name} car is running at speed of {self.top_speed}")

    def car_company(self):
        print(f"{self.name} car is from {self.company}")

    def car_model(self):
        print(f"{self.company} car with model {self.model} has completed the test")

bmw = Car()
bmw.name = "BMW"
bmw.color = "Red"
bmw.model = "X3"
bmw.top_speed = "125 km/hr"
bmw.company = "TATA"

bmw.car_start()
bmw.car_running()
bmw.car_speed()
bmw.car_company()
bmw.car_model()