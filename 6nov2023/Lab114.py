class Person:
    def __init__(self, name):
        self.name = name
        print("you created an object")

    def print_details(self,name):
        print("Your details are ->", self.name)

    def print_details2(self):
        print("Your details are ->", self.name*2)


amit = Person("Amit")
amit.print_details("Amit")
amit.print_details2()

Nikhil = Person("Nikhil")
Nikhil.print_details("AMit")
Nikhil.print_details2()
