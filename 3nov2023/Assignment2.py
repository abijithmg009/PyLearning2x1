#Create a Class Person , Two Objects by taking (name, age, address) Input from users and print details in the end.

class Person:
    name = None
    age = None
    address = None

    def print_details(self):
        print(f"The {self.name} has age of {self.age} is living in address {self.address}")



object_details = Person()
object_details.name = "Abijith"
object_details.age = 31
object_details.address = "Midhila House Marathakkara"
object_details.print_details()