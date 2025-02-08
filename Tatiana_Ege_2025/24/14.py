import re
s = open(r'C:\Users\Zarif\Desktop\demo_2025_24.txt').readline()
s = s.replace('--', '**')
s = s.replace('*-', '**')
s = s.replace('-*', '**')
s = s.replace('-', '*')
s = s.split('*')
mxln = 0
ln = 0
zn = 0
for x in s:
    zn += 1
    if len(x) > 0:
        if x[0] != '0':
            ln += len(x)
        elif x == '0':
            ln += 1
        elif x[0] == '0':
            mxln = max(mxln, ln + zn - 2)
            ln = 0
            zn = 0
    else:
        mxln = max(mxln, ln + zn - 2)
        ln = 0
        zn = 0
print(mxln)
# m = re.findall(r'(?:(?:[1-9]\d*|0)[-*])+(?:[1-9]\d*|0)', s)
# print(max(m, key=len))
# print(len(max(m, key=len)))
