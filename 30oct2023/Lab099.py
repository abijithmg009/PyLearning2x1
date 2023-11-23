#orderedDict

my_dict = {'b':45, 'a':65, 'c':87},#its unordered list
print(my_dict)

#Ordered Dict is special, based on key value assertion

from collections import OrderedDict
od = OrderedDict()

od['a']=45
od['d']=73
od['c']= 75
od['b']= 55

print(od)

#Dictionary has no slicing which is only available on list

#Selenium - insert webelments into a Dict
# You want to keep the order - login elements, Dashboard elements


#Dict = it will not keep  the order of insertion
#OrderedDict = it will keep the order of insertion

keys = list(od.keys())
print(keys)
keys_sorted = sorted(keys)
print(keys_sorted)

od2 = OrderedDict()
od2[keys_sorted[0]]=45
od2[keys_sorted[1]]=43
od2[keys_sorted[2]]=76
od2[keys_sorted[3]]=67
print(od2)


keys_reversd = list(reversed(keys_sorted))
print(keys_reversd)