#continue will skip the loop and increment will do
for i in range(1,10):
    if(i%2 == 0):
        print(f"found an even number : {i}")
        continue
    print(f"found an odd number:{i}")