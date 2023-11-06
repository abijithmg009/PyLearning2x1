# Map and Filter

square = lambda x: x * x
result = square(5)
print(result)

# map -
numbers = [1, 2, 3, 4, 5]
sq_numbers = []

for i in numbers:
    sq_numbers.append(square(i))
print(sq_numbers)
print(type(sq_numbers))

# this can be avoid using map function and one linear

sq_numbers2 = list(map(lambda x: x * x, numbers))
print(sq_numbers2)


def tripe(a):
    return (a * 3)


triple = list(map(tripe, numbers))
# pick each element from numbers and use the triple function
print(triple)
# advisable to use with lambda expression, but other functions can be used.
