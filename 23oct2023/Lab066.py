orginal_str = "PRAMOD"
rev_str = orginal_str[::-1]
#[start, stop, step], start dedult value is 0, stop default value is len, and step -1 which will reverse the string
print(rev_str)
user_input = input("Enter the string\n")
def palindrome(user_input):
    rev_str = user_input[::-1]
    return rev_str

palindrome(user_input)
print(rev_str)
if rev_str==user_input:
    print("palindrome")
else:
    print("not a palindrome")
