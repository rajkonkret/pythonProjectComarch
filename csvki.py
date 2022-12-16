import csv

fields = ["name", "branch", "year", "cgpa"]
rows = ["Sanchit", "COE", "2", "9.1"]

my_dict = [
    {'branch': 'COE', 'cgpa': '9.1', 'name': 'Nikhil', 'year': 2},
    {'branch': 'COS', 'cgpa': '6.1', 'name': 'rdek', 'year': 3}
]

file = 'records2.csv'

with open(file, 'w', newline='') as csv_f:
    csvwriter = csv.DictWriter(csv_f, fieldnames=fields)
    csvwriter.writeheader()
    csvwriter.writerows(my_dict)
