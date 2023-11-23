#Filters
numbers = [1,2,3,4,5,6,7,8,9,10]
even_numbers = []
#filter -> will have less number of elements or equal to


def isEven(num):
    return num%2==0

op = isEven(2)
print(op)

even_numbers = filter(isEven,numbers)
print(even_numbers)
even_numbers_list = list(even_numbers)
print(even_numbers_list)
