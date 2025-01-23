import re
# s = open('1088_1.txt').readline().replace('CD', '#')
# m = re.findall(r'(?:\w*#){160}\w*', s)
# print(len(max(m, key=len)) + 160 + 2)
s = open('1088_1.txt').readline().split('CD')
print(s)
mx = 0
for x in range(len(s) - 160):
    ln = 0
    for y in range(0, 161):
        ln += len(s[x + y])
    mx = max(mx, ln)
print(mx + 2 * 160 + 2)
