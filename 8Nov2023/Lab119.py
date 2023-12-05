
#encapsulation setup, getter setter technique,
class Password:

    def __init__(self, password):
        self.__password = password

    def get_password(self, is_Auth):
        if is_Auth:
            return self.__password
        else:
            print("You're not authenticated")



    def set_password(self, password):

        if len(password) > 10:
            self.__password = password
            print(len(password))
        else:
            print("weak password")
            print(len(password))



    def print_len(self):
        print("Your password length is ", len(self.__password))


pwd = Password("Hacker123")
pwd.print_len()
# we cannot change the password here as it is private

pwd_s = pwd.get_password(False)
print(pwd_s)

pwd.set_password("pramod123123")
