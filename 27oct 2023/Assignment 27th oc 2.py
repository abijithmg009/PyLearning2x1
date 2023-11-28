#3. Write a Python program to sum all numbers in a list.

my_list2 = [24,5,6,76,5,35,54,45,67,7,77]
total = 0
for i in my_list2:
    total = total+i

print(f"The total in the given list is {total}")


#4. Write a Python program to multiply all numbers in a list
my_list3 = [23,45,67,88,97,87,87,77,45]
mul = 1

for i in my_list3:
    mul = mul * i

print(mul)


#5. Write a Python program to count the number of strings in a list where the string length is 2 or more and
# the first and last character are the same.
lstStr = ["str","asda","aaaa","ssar","aawera","aa","aaawa"]
count = 0
for x in lstStr:
    if len(x) >= 2 and x[0] == x[len(x)-1]:
        count += 1

print(count)
