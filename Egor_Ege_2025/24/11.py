s = open(r'C:\Users\Zarif\Downloads\340_1 (3).txt').readline()
gl = 'EYUIOA'
sogl = 'QWRTPSDFGHJKLZXCVBNM'
for x in sogl:
        s = s.replace(x, '1')
for y in gl:
        s = s.replace(y, '0')
mxln = 0
ln = 1
for x in range(len(s) - 1):
    if s[x] != s[x + 1]:
        ln += 1
        mxln = max(mxln, ln)
    else:
        ln = 1
print(mxln)