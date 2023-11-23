#Task 1
"""
Palindrome Checker:
Create a function that checks if a given string is a palindrome (reads the same forwards and backward). 121

Example - pramod
madam - reverse(madam) -> same
Naman -> reverse -> same
Malayalam

Compare String with the Revserse of the string
"""
def is_palindrome(string1):
    if string1 == string1[::-1]:
        print(f"{string1} is palindrome")
    else:
        print(f"{string1} is not palindrome")


str1 = input("Enter a string: ")

is_palindrome(str1)
"""
Task #2

Sum of Digits: Create a function that calculates the sum of the digits of a positive integer.
n = 12345
sum = 15
n = 123
sum = 6
"""


def get_sum(num):
    sum1 = 0
    while num != 0:
        sum1 = sum1 + (num % 10)
        num = num // 10

    return sum1


n = int(input("Enter a positive integer: "))
print(get_sum(n))


