s = open(r'C:\Users\Zarif\Downloads\1618_1 (5).txt').readlines()
ct = 0
for x in s:
    x = x.strip() # AOA   > OAO
    if x.count('AOA') > x.count('OAO'):
        ct += 1
print(ct)