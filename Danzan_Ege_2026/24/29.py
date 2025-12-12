import re
s = open(r'C:\Users\Zarif\Downloads\1172_1 (7).txt').readline()
m = re.findall(r'(?:[1-9][0-9]*[+*])+[1-9][0-9]*', s)
for x in m:
    if x.count('*') + x.count('+') == 43:
        print(x)
# print(max(m, key = len))
# print(len(max(m, key = len)))
# 7003870