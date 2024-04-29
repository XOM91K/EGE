s = open(r'C:\Users\Zarif\Downloads\24_614_1.txt').readlines()
ct = 0
for x in s:
    if x.count('E') > x.count('A'):
        ct += 1
print(ct)