

class Details:

    def __init__(self, name):
        self.__name = name

    def get_name(self, is_Auth):
        if is_Auth:
            return(self.__name)
        else:
            print("You're not authenticated")
    def set_name(self,name):
        if len(name) > 10:
            self.__name = name
            print("The length of name",len(self.__name), self.__name)
        else:
            print("TOO small name")
            print("The length of name", len(self.__name), self.__name)

student = Details("Temp")
student.set_name("Two")
print(student.get_name(True))

