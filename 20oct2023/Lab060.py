num = int(input("Enter a number\n"))
match num:
    case 10: #condition based is not possible
        print("10")
    case _:
        print("default")
