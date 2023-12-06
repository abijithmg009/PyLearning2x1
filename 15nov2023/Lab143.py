
def main():
    print("Hello from main")


if __name__ == "__main__":
    main()

# we will get run command for the above command.


# collections-
"""
List, dict, tuple, set,
Alternatives Python general purpose containers - Advanced - Counter, ordered set.
we are okay with the general purpose containers in Python
"""

reg = (1,2,3) #tuple not muttable
list_var = [1,2,3]
print(type(reg))

from collections import namedtuple

person = namedtuple("Person",["name", "age", "gender"])

person = person(name = "Pramod", age= 34, gender= "Male")
print("name", person.name)
print("Age", person.age)
print("Gender", person.gender)

# no need we can use a class instead


class Person1:
    def __init__(self, name, age, gender):
        self.name = "Pramod"
        self.age = 34
        self.gender = "M"

    def print_details(self):
        print(f"Person details are name {self.name} with {self.age} age with {self.gender} gender")

Person2 = Person1("Pramod", 34, "M")
Person2.print_details()