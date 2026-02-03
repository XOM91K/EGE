import re
s = open('39.txt').readlines()
ct = 0
for x in s:
    x = x.strip()
    m = re.findall(r'Q\w*W\w*E\w*R\w*T\w*Y', x)
    if len(m) > 0:
        ct += 1
print(ct)