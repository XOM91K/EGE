import re
l=open(r'C:\Users\Zarif\Downloads\1617_1 (2).txt').readlines()
ct = 0
for x in l:
    x = x.strip()
    m=re.findall(r'\w*Q\w*W\w*E\w*R\w*T\w*Y', x)
    if m:
        print(m)
        ct += 1
print(ct)