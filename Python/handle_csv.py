import csv
with open("students.csv", mode='w', newline='') as file:
    writer=csv.writer(file)
    writer.writerow(['NAME', 'AGE', 'GRADE'])
    writer.writerow(['Alice', 23, '1st'])
    writer.writerow(['Anuska', 21, '2nd'])

with open('students.csv', mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
