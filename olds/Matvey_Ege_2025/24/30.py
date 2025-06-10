import re
s = open(r'C:\Users\Zarif\Downloads\1458_1 (1).txt').readline()
m = re.findall(r'\((?:[1-4]+\+)+[1-4]+\)', s)
mx_ln = []
for x in m:
    if eval(x[1:-1]) % 2 == 0:
        mx_ln.append(len(x))
print(max(mx_ln))