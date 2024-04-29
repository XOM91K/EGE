#s = open(r'C:\Users\Zarif\Downloads\24_162_1.txt').readline()
s = open(r'C:\Users\Zarif\Desktop\24-181.txt').readline()
# WD.QDQQQQQQWQWD.WDQQQQQQQQQQQQQQWDqQW.QQWD.QDWWWDW.QWDQWD
s = s.split('.')
mx = 0
for x in range(len(s) - 3):
    mx = max(mx, len(s[x] + s[x + 1] + s[x + 2] + s[x + 3]) + 3)
print(mx)