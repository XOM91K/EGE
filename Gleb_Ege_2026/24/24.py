import re
s = open(r'C:\Users\Zarif\Downloads\1647_1 (4).txt').readline()
m = re.findall(r'(?:[1-9]\d*[+*])+[1-9]\d*', s)
mx = []
for x in m:
    if eval(x) % 2 == 0:
        mx.append(len(x))
print(max(mx))