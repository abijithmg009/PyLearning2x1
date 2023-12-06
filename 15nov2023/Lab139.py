# try except
# try except else finally
try:
    print(10 / 0)
except ZeroDivisionError as E:
    print(E)

# try except else finally
try:
    num1 = int(input("Enter a number\n"))
    num2 = int(input("Enter 2nd number\n"))
    result = num1 / num2
except ValueError:
    print("Invalid input")
except ZeroDivisionError:
    print("num2 is zero")
except Exception:
    print("Error")
else:
    print(f"Result is {result}")
finally:
    print("I will be always executed")

# Error, if num1 as 10 and num2 as 0, it will show error, zero division error
# , if we enter string it can value error.
