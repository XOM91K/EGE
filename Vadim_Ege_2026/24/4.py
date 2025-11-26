import re
s = open(r'C:\Users\Zarif\Downloads\339_1 (8).txt').readline()
s = s.split('F')
mx = 0
for x in range(len(s) - 1):
    mx = max(mx, len(s[x] + s[x + 1]) + 1)
print(mx)
# m = re.findall(r'[DE]+F[DE]+', s)
# print(len(max(m, key=len)))
