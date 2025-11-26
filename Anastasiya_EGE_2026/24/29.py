import re
s = open(r'C:\Users\Zarif\Downloads\339_1 (10).txt').readline()
s = s.split('F')
mx_ln = 0
for x in range(len(s) - 1):
    mx_ln = max(mx_ln, len(s[x] + s[x + 1]))
print(mx_ln)
# m = re.findall(r'[DE]+F[DE]+', s)
# print(len(max(m, key=len)))