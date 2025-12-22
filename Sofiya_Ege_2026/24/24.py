import re
t=open(r'C:\Users\Zarif\Downloads\1458_1 (5).txt').readline()
m=re.findall(r'\((?:[1234]+\+)+[1234]+\)', t)
mx = []
for x in m:
    if eval(x) % 2 == 0:
        mx.append(len(x))
print(max(mx))