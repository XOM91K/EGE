s = open(r'C:\Users\Zarif\Downloads\1483_1 (4).txt').readline()
s = s.split('CDE')
mn = 10 ** 10
for x in range(len(s) - 85):
    ln = 0
    for y in range(86):
        ln += len(s[x + y])
    mn = min(mn, ln + 87 * 3)
print(mn)