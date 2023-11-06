squares = [2,4,9,16,25]

l = squares # here no new list is created that's the reason, if we change the value in intial list it reflect here
l2 = squares.copy() #here we are creating new list and new changes in inital list will not effect

squares[0] = 33

print(l)
print(l2)