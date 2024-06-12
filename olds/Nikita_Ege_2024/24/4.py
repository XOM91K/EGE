s = open(r'C:\Users\Zarif\Downloads\24_615_1.txt').readlines()
ct = 0
for x in s:
    if x.count('A') > x.count('E'):
        ct += 1
print(ct)