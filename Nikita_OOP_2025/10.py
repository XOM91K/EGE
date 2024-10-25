import csv
n = int(input())
with open('vps.csv', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter=';', quotechar='"')
    for index, row in enumerate(reader):
        if int(row[-2]) > n:
            print(row[0])