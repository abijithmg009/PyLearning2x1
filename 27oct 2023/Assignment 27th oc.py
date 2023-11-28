# 1. Write a Python program to find the largest number in a list.

my_list = [23,5,65,76,54,66,57,66,76,46]


def find_max(list):
    max = list[0]
    for i in list:
        if i>max:
            max= i
        else:
            pass
    return max


op = find_max(my_list)
print(op)



#2. Write a Python program to find the smallest number in a list.

my_list1 = [23,45,67,89,67,87,76,76,87,46,96]

def find_min(list):
    min = list[0]
    for i in list:
        if i<min:
            min = i
        else:
            pass
    return min

op = find_min(my_list1)
print(op)

