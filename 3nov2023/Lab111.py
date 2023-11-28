def sum(a,b):
    c = a+b
    print(c)

class MyClass:
    name = None


    def print_my_name_lastname(self, last_name, age):
        print("Your name is " + self.name, last_name, age)

abijith_obj = MyClass()
abijith_obj.name = "Abijith"
abijith_obj.print_my_name_lastname("MG",35)