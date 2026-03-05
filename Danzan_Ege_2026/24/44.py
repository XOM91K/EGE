import re
s = open(r'C:\Users\Zarif\Downloads\511_1 (4).txt').readline()
m = re.findall(r'(?:(?:[1-9][0-9]*|0)[*+])+(?:[1-9][0-9]*|0)', s)
mx = []
for x in m:
    if eval(x) == 0:
        mx.append(len(x))
print(max(mx))