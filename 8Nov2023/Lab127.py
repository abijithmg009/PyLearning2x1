
class GF:
    def car(self):
        return "Old Car"

class F(GF):
    #def car(self):
     #   return "Basic Car"
     pass

class S(F):
    #def car(self):
     #   return "Hybrid Car"
     pass

Son = S()
print(Son.car()) # son has highest priority then father, from bottom to up