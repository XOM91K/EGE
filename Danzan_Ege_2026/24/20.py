import re
s = open(r'C:\Users\Zarif\Downloads\339_1 (11).txt').readline()
s = s.split('F')
mx_ln = []
for x in range(len(s) - 1):
    mx_ln.append(len(s[x]) + len(s[x + 1]))
print(max(mx_ln))
# m = re.findall(r'[^F]+F[^F]+', s)
# print(max(m, key=len))
# print(len(max(m, key=len)))