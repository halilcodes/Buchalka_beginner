import csv
import pandas as pd

with open('OlympicMedals_2020.csv', encoding='utf-8', newline='') as csv_file:
    sample = ""
    for line in range(3):
        sample = csv_file.readline()
    medals_dialect = csv.Sniffer().sniff(sample)
    csv_file.seek(0)
    medals = csv.reader(csv_file, dialect=medals_dialect)
    for row in medals:
        print(row)
    print('*' * 80)
    csv_file.seek(0)
    df = pd.read_csv(csv_file)
    # df = pd.read_csv('OlympicMedals_2020.csv')
    print(df)

# df = pd.read_csv('OlympicMedals_2020.csv')
# print(df)
# print('*' * 80)
# print(df[df['Rank'] == 86])
