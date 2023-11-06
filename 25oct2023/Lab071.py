#list
# Collection of items and duplicate is allowed.

my_list = [1,2,5]
my_list2 = [1,True, "Pramod"]

print("initial list",my_list)


#chaning the element

my_list[2]= 34
print("list after adding ",my_list)

#append
my_list.append(45)

print("list after appending  ",my_list)

#Extend ; which will join two list
my_list.extend([67,89])
print("list after extending ",my_list)

#Inserting
my_list.insert(4,'b')
print("list after inserting ",my_list)
# it will insert in that index and the other values will move from right after that.


#remove
my_list.remove('b')
print("list after removing ",my_list)

#copy

my_list_copy = my_list.copy()
print("list after after ",my_list_copy)

#clear
my_list.clear()
print("list after clearing ",my_list)
#sort
my_list_copy.sort()
print(my_list_copy)
my_list_copy.reverse()
print(my_list_copy)

print(my_list_copy[0])
print(my_list_copy[1])
print(my_list_copy[2])
print(my_list_copy[3])
print(my_list_copy[4])

print(len(my_list_copy))








