import re
t=open('1566_1.txt').readline()
m=re.findall(r'\d\d[A-Z]', t)
print(len(max(m, key=len)))