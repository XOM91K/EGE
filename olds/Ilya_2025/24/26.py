import re
# s = open(r'C:\Users\Zarif\Downloads\1062_1 (1).txt').readline().replace('FGSW', '#')
# m = re.findall(r'(?:\w+#){85}\w+', s)
# print(len(max(m, key=len)) + 3 * 85 + 6)
# print(max(m, key=len)) # 1361
s = open(r'C:\Users\Zarif\Downloads\1062_1 (1).txt').readline().replace('FGSW', '#')
s = s.split('#')
mx_ln = 0
for x in range(len(s) - 85):
    ln = 0
    for y in range(0, 86):
        ln += len(s[x + y])
    mx_ln = max(mx_ln, ln)
print(mx_ln + 4 * 85 + 6)
#1447