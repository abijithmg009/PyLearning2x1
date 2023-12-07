import csv

temp_data = []
id_update = 2
new_age = 26

with open('Sathish.csv', 'r') as file_csv:
    reader = csv.reader(file_csv)
    for row in reader:
        temp_data.append(row)


#for row in temp_data:
 #   if row[0] == id_update:
  #      row[2] = new_age


temp_data[1][2] = 26
print(temp_data)
with open('Sathish.csv', 'w', newline='') as new_file_csv:
    writer = csv.writer(new_file_csv)
    writer.writerows(temp_data)

