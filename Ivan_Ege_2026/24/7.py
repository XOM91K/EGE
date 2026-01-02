import re
s = open(r'328_1 (6).txt').readline()
s = s.split('CD')
mx = []
for x in range(len(s) - 50):
    ln = ''
    for y in range(0, 51):
        ln += s[x + y] + 'CD'
    mx.append(ln[:-2])
print(len(max(mx, key=len)))
# s = s.replace('CD', '#')
# m = re.findall(r'(?:[^#]*#){50}[^#]*', s)
# print(len(max(m, key=len)) + 50 + 2)
# CCCCCCCCCCCCCCCCD