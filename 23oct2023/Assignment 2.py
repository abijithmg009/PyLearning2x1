"""
✅ Right Triangle Star Pattern

*
**
***
****
*****
"""


n = int(input("enter the number to form pyramid:"))
for i in range(n):
    for j in range(i+1):
          print("*",end=" ")
    print("")
