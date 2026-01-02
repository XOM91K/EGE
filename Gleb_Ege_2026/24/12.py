import re
s = open(r'C:\Users\Zarif\Downloads\1458_1 (7).txt').readline()
m = re.findall(r'\((?:\d+\+)+\d+\)', s)
mx_ln = []
for x in m:
    if eval(x) % 2 == 0:
        mx_ln.append(len(x))
print(max(mx_ln))