user_input = input("Enter the user input\n")
#Palindrome
#if we reverse the strign and it matches with intial one, then it is Palindrome

#1. by tdaritional method
#2 by build in functions

def reverse_string(user_input):
    reverse_str = ""
    for char in user_input:
        reverse_str = char+reverse_str

    return reverse_str



rev_string = reverse_string(user_input)
print(rev_string)

if rev_string==user_input:
    print("Palindrome")
else:
    print("not a palindrome")