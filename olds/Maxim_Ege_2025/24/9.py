s = open(r'C:\Users\Zarif\Downloads\1483_1 (2).txt').readline()
#s = open(r'9.txt').readline()
s = s.split('CDE')
mnln = 10 ** 10
for x in range(len(s) - 86):
    ln = 0
    for y in range(0, 86):
        ln += len(s[x + y])
    k = 0
    for y in s[x + 2]:
        if y == 'E':
            k += 1
        else:
            k += 1
            break
    else:
        k += 1
    mnln = min(mnln, ln + 3 * 87 + k)
print(mnln)