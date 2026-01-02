import re
s = open(r'C:\Users\Zarif\Downloads\1458_1 (6).txt').readline()
m = re.findall(r'\((?:\d+\+)+\d+\)', s)
mx = []
for x in m:
    if eval(x) % 2 == 0:
        mx.append(len(x))
print(max(mx))