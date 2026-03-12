import re
t=open(r'C:\Users\Zarif\Downloads\1647_1 (2).txt').readline()
m=re.findall(r'(?=((?:(?:[1-9][0-9]*|0)[*+])+(?:[1-9][0-9]*|0)))', t)
chet = []
print(len(m))
for x in m:
    if eval(x) % 2 == 0:
        chet.append(x)
print(len(max(chet, key=len)))
print(max(chet, key=len))