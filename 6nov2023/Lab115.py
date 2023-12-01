#Encapsulation
#Data members and Methods together
import self


#Visibility
#public
#Protected
#Privite variable


class My_Class:

    def __init__(self):
        self.public_var = 10
        self._Protected_var = 12
        self.__Private_var = 15


    def public_method(self):
        print("This is public method")
        print("only I can see the private variable", self.__Private_var)

    def _protected_method(self):
        print("this is protected method")
        print(self.__Private_var)
        print(self._Protected_var)

    def __private_method(self):
        print("This is private method")
        print(self.__Private_var)
        print(self._Protected_var)

obj = My_Class()
print(obj.public_var)
print(obj._Protected_var)
#print(obj.__Private__var) # can be used in class itself and it's functions not outside.
obj.public_method()
obj._protected_method()
obj.__private_method() #Will not able to call as it is private method
