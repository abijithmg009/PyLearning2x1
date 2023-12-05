

class Bank:
    def __init__(self):
        self.balance = 0 #instance variable (you can access it via only object)
        self.__private_var = 10

    def deposit(self,amount): # public function
        self.balance = self.balance + amount
        # self.amount = self.balance+amount

    def _withdraw(self,amount): #protected
        self.balance = self.balance- amount

    def __balance(self):
        print("Your balance", self.balance)

    def is_Auth_True(self,Auth):
        if Auth:
            self.__balance()
        else:
            print("You're not authenticated")



    def with_draw_by_manager(self, amount):
        self._withdraw(amount=amount)


jp_chase = Bank()
jp_chase.deposit(1000)
jp_chase._withdraw(499) # not a good practice
#jp_chase.__balance() #cannot be accessible directly only using an internal public function
#write the code to authenticate, then we can call the private variable using a public function

jp_chase._BankAccount__private_var = 100
print(jp_chase._BankAccount__private_var) # Super bad practice, Python allow this, but not Java

jp_chase.is_Auth_True(True)
