import csv

data =  [
    ['Name', 'Age', 'City'],
    ['Alice', 45, 'Texes'],
    ['Peter', 56, 'NY']
]

with open('mydata.csv', 'w') as file:
    writer = csv.writer(file)
    for row in data:
        writer.writerow(row)


"""
Most of time, 90% nwe will read the time,10% we will write the file

"""
