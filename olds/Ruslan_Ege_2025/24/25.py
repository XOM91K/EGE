import re

s = open(r'C:\Users\Zarif\Downloads\1172_1 (4).txt').readline()
m = re.findall(r'(?:[1-9]\d*[+*])+[1-9]\d*', s)
mx_chisel = 0
for x in m:
    mx_chisel = max(mx_chisel, x.count('*') + x.count('+') + 1)
print(mx_chisel)
# d = max(m, key=lambda d: len(d.replace('*', ' ').replace('+', ' ').split()))
# print(d)
# d = str(d).replace('*', ' ').replace('+', ' ')
# b = d.split()
# print(len(b))
# # print(d)
# # 5+5+5