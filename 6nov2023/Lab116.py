
class My_class:
    def __init__(self):
        self.__private_toilet = "Private toilet only pramod allowed"
        self._protected_toilet = "Protected toilet, access restricted"
        self.public_toilet = "Public toilet"

    def __private_method(self):
        return "This is a private method"


obj = My_class()
#print(obj._My_class__private_toilet)
#obj.__private_method()
print(obj._protected_toilet)
print(obj.public_toilet)