#F, M -> S - Multple level

class Father:

    def father_money(self):
        return 5

class Mother:
    def mother_money(self):
        return 5

class Son(Father,Mother):
    pass


son = Son()
print(son.father_money())
print(son.mother_money())
Total = son.father_money()+son.mother_money()
print("Total Son has is", Total)
