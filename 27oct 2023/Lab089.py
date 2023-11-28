t=("TheTestingAcademy","for","TheTestingAcademy")
print("\nSet with the use of Tuple: ")
print(set(t))
# output order may change after some runs.

set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}
my_set = set1.union(set2)
print(my_set)
my_set1 = set1.intersection(set2)
print(my_set1)

my_set2 = set1.difference(set2)
my_set3 = set2.difference(set1)
print(my_set2)
print(my_set3)


set1 = {1,2,3,4,5}
set2 = {4,3,2}
subset = set2.issubset(set1)
print(subset)
#can we do on list
l = [1,2,3,4,5]
#not possible with list


set1 = set(["TheTestingAcademy", "For", "TheTestingAcademy."])
print(set1)

for i in set1:
    print(i)


set1 = set([1, 2, 3, 4, 5, 6,
            7, 8, 9, 10, 11, 12])


set1.remove(5)
set1.remove(6)
print(set1)







