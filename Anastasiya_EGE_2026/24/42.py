m = open('42.txt').readlines()
ct = 0
for x in m:
    x = x.strip()
    if x.count('AOA') > x.count('OAO'):
        ct += 1
print(ct)