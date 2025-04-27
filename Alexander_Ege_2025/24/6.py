import re
s = open(r'C:\Users\Zarif\Downloads\339_1 (6).txt').readline()
#s = open(r'6.txt').readline()
m = re.findall(r'[DE]+F?[DE]+', s)
print(len(max(m, key=len)))
s = s.split('F')
mx_ln = []
for x in range(len(s) - 1):
    mx_ln.append(len(s[x]) + len(s[x + 1]) + 1)
print(max(mx_ln))