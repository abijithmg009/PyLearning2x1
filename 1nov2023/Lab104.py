numbers = [1,-2,3,-4,5,6,-7,8,-9,10]


def if_Positive(num):
    return num>0


postive_numbers = filter(if_Positive,numbers)
print(postive_numbers)
postive_numbers_list = list(postive_numbers)
print(postive_numbers_list)

#map will apply function on all elements, but filter will filter out the result
#map it will return always same number of elements
