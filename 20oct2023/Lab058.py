#Match statment
# we don't have switch statement in Python, Match statement is similar to switch

number = int(input("enter your number\n"))

match number:
    case 1:
        print("You have entered 1")
    case 2:
        print("you have entered 2")
    case _:
        print("No idea")