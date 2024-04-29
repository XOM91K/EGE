import re
s = open(r'C:\Users\Zarif\Downloads\24_619_1 (4).txt').readlines()
ct = 0
for x in s:
    m = re.findall(r"Z[A-Z]RO", x)
    if len(m) != 0:
        ct += 1
print(ct)