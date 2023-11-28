#Take a input from user, and

class Car:
    color = None
    model = None

    def car_details(self):
        print("Your car details is " + self.color, self.model)

car_color = input("Enter the color of car \n")
car_model = input("Enter your car model \n")

car_obj = Car()
car_obj.color = car_color
car_obj.model = car_model
car_obj.car_details()