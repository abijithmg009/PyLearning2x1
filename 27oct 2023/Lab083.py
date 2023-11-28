my_list = [1,2,3,4,5,6,7,8,8,8]
print(my_list)
my_list[2] = 20
print(my_list)
print(type(my_list))


"""
Tuple : is same as collection of items.
Tuple()
List[]
can have duplicats
"""
car = (True, "Hector", 123, 123,123)
print(car)
print(type(car))
#car[1] = "Tractor"
"""
Once you created, and we can't chage after word
"""
print(len(car))


#List can be converted to Tuple
list1 = [1,2,3,4,5,6]
print(tuple(list1))