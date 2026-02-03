import re
s = open('28.txt').readlines()
print(s)
ct = 0
for x in s:
    x = x.strip()
    m = re.findall('Q\w*W\w*E\w*R\w*T\w*Y', x)
    if len(m) > 0:
        print(m)
        ct += 1
print(ct)