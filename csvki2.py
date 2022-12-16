import csv

filename = 'records2.csv'

fields = []
rows = []

with open(filename, 'r') as csv_file:
    csvreader = csv.reader(csv_file, delimiter=',')

    fields = next(csvreader)
    for row in csvreader:
        rows.append(row)
    print("Suma wierszy", csvreader.line_num)

print(fields)
print(rows)

for row in rows:
    print(row)
    print(type(row))
    print(row[0])
