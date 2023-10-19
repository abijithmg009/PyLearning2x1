# break and continue
#it will come out of loop if the conditoon met

count = 1
while count <= 10:
    print(count)
    if count == 5:
        break
    count = count + 1


for counter in range(1,10):
    if counter==5:
        break
    print(counter)