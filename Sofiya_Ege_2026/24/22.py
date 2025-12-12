import re
s=open(r'C:\Users\Zarif\Downloads\1022_1.txt').readline()
s=s.replace('FSRQ', '#')
s = s.split('#')
mx = []
for x in range(len(s) - 80):
    ln = 0
    for y in range(0, 81):
        ln += len(s[x + y])
    mx.append(ln)
# m=re.finditer(r'(?=((?:\w*#){80}\w*))', s)
# mx=[]
# for x in m:
#     mx.append(len(x.group(1)))
# print(max(mx))
print(max(mx) + 4 * 80 + 6)