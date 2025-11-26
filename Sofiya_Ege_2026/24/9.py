# import re
t=open(r'C:\Users\Zarif\Downloads\339_1 (9).txt').readline()
t = t.split('F')
mx_ln = 0
for x in range(len(t) - 1):
    mx_ln = max(mx_ln, len(t[x] + t[x + 1]))
print(mx_ln + 1)
# m=re.findall(r'[DE]*F[DE]*', t)
# print(len(max(m, key=len)))