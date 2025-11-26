import re
s = open(r'C:\Users\Zarif\Downloads\403_1 (7).txt').readline()
for x in range(10):
    s = s.replace('XXXX', 'XX XX')
    s = s.replace('YYYY', 'YY YY')
    s = s.replace('ZZZZ', 'ZZ ZZ')
s = s.split()
print(s)
mx = 0
for x in s:
    m = re.findall(r'(?:XX|YY|ZZ)+', x)
    mx = max(mx, len(max(m, key=len)))

print(mx)