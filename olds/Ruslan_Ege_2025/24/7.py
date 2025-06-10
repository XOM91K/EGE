import re
s = [x.strip() for x in open(r'C:\Users\Zarif\Downloads\176_1 (2).txt')]
ct = 0
for x in s:
    m = re.findall(r'195\.2[0-5]?\d\.(?:1\d{0,2}|2[0-5]{0,2})\.14', x)
    if len(m) > 0:
        print(x)
        ct += 1
print(ct)