import csv

cereals_filename = "my_cereals.csv"

with open(cereals_filename, encoding='UTF8', newline='') as cereals_file:
    reader = csv.DictReader(cereals_file)
    for row in reader:
        print(row)
