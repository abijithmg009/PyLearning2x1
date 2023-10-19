#Triangle Classifier:

side1 = float(input("enter the first side\n"))
side2 = float(input("enter the second side\n"))
side3 = float(input("enter the third side\n"))

if side1==side2==side3:
    print("Equilateral Triangle")
elif side1==2 or side1==side3 or side2==side3:
    print("Isosless triangle")
else:
    print("Scaler triangle")
