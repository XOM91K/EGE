import re
s = open(r'C:\Users\Zarif\Downloads\24_10724 (1).txt').readline()
alf = '123456789ABCDEF'
zeroFlag = False
ct = mx = 0
for x in range(len(s)):
    if (s[x] == '0' and zeroFlag == True) or (s[x] in alf):
        ct += 1
        zeroFlag = True
    elif s[x] not in alf:
        mx = max(mx, ct)
        ct = 0
        zeroFlag = False
print(mx)


