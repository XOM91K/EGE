import re
s = open('8.txt').readline().split('AF')
mn = 10 ** 10
for i in range(len(s) - 199):
    ln = sum([len(s[i + j])for j in range(200)])
    mn = min(mn, ln + 402)
print(mn)
# m = re.findall('(?:\w*?AF\w*?){201}', s)
# print(max(m, key=len))