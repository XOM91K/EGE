s = open('38.txt').readlines()
ct = 0
for x in s:
    x = x.strip()
    if x.count('AOA') > x.count('OAO'):
        ct += 1
print(ct)
