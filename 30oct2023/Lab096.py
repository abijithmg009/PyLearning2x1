my_dict = {'a':7,'b':72,'c':82,'a':95}
print(my_dict) #latest value will take for a which is 95

keys = my_dict.keys()
value = my_dict.values()
print(keys)
print(value)

key_list = list(keys) # to convert to list

print(key_list[2])
#my_dict.cler() # which will clear dictonary


copy_my_dict = my_dict.copy()
print(copy_my_dict)



