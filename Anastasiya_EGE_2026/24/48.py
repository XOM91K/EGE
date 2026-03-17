import re
s = open(r'C:\Users\Zarif\Downloads\403_1 (9).txt').readline()
m = re.findall(r'(?=((?:XX|YY|ZZ)+))', s)
mx = []
for x in m:
    if 'XXXX' not in x and 'YYYY' not in x and 'ZZZZ' not in x:
        mx.append(len(x))
print(max(mx))