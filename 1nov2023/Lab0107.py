numList = [30, 2, -15, 17, 9, 100]

def num_greater_10(num):
    return  num>10

list_of_numbers = list(filter(num_greater_10,numList))
print(list_of_numbers)


list_numbers_lam = list(filter(lambda num:num>10, numList))
print(list_numbers_lam)

numbers_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
#tuples are immutable, can't be changed, list is muttable in nature
def is_even(num):
    return num % 2 == 0


even_numbers_tuple = tuple(filter(is_even, numbers_tuple))
print(even_numbers_tuple)

#can add tuple inside list
l = [(1, 23), (34, 34)]
print(l)
print(l[0])
print(l[0][0])
print(l[0][1])