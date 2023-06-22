import csv
import pandas as pd

with open('cereal_grains.csv', newline='', encoding='utf-8') as csv_file:
    reader = csv.reader(csv_file, quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:
        print(row)

print("*" * 80)
