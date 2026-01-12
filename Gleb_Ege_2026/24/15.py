s = open(r'C:\Users\Zarif\Downloads\1483_1 (9).txt').readline()
s = s.split('CDE')
mx = []
for x in range(len(s) - 85):
    ln = 0
    for y in range(0, 86):
        ln += len(s[x + y])
    mx.append(ln)
print(min(mx) + 87 * 3)