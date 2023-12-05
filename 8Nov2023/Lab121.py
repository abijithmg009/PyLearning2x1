#Single Inheritence = 98%
#use the properties and methods of base class/parent class to a child class.


class Father:
    bank_bal = 100

    def one_bhk(auth):
        if (auth==True):
            print ("take it")
        else:
            print("you're not Authorized")
class Son(Father):
    pass


s = Son()
s.one_bhk(True)
print(s.bank_bal)