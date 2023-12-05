#protected - out of Module is restricted,
#public can be accessible in another module
#private now way.

# Public variable - Don't mention anything
# Protected - _
#private - __
# we can make both variable and function the above things.


class Person:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name
    def set_name(self, name):
        if name == "John":
            print(" Don't set the name")
        else:
            self.__name = name

    def print_details(self):
        print("Your details is", self.__age, self.__name)



person = Person("Abhijith", 30)
person.print_details()
#print(person.__name) will not able to fetch the value or set any value
# if we want to access the private variable, we have to use another public fucntion, get set

person.set_name("John")
person.get_name()





