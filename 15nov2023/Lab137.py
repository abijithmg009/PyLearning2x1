#Exception is an abnormal event, during the execution of program, which can be handled
# Error - Specific piece of code which cause an issue, very difficult to overcome
#Memmory error - restart, retry

try:
    print(10 / 0)
except ZeroDivisionError as error:
    print("Error", error)


