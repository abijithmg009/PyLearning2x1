#is palindrome with Lambda
orginal_str = "malayalam"
rev_string = lambda orginal_str:orginal_str[::-1]

if rev_string==orginal_str:
    print("Palindrome")
else:
    print("Not a Palindrome")