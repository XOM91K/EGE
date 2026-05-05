import re
t=open(r'C:\Users\Zarif\Downloads\1172_1 (8).txt').readline()
m=re.findall(r'(?:[1-9][0-9]*[*+])+[1-9][0-9]*', t)
s = max(m, key=lambda s: (s.count('*') + s.count('+')))
print(s.count('*') + s.count('+') + 1)