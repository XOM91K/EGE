import csv

school_number, class_number = map(int, input().split())
results = []

with open('rez.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file, delimiter=',')
    for row in reader:
        login_parts = row['login'].split('-')
        if int(login_parts[2]) == school_number and int(login_parts[3]) == class_number:
            results.append((row['user_name'], int(row['Score'])))
results = sorted(results, key=lambda d: d[0])[::-1]
results = sorted(results, key=lambda d: -d[1])

for name, score in results:
    last_name = name.split()[-2]
    print(f"{last_name} {score}")