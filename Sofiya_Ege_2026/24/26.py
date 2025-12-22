s=open(r'C:\Users\Zarif\Downloads\1483_1 (6).txt').readline()
s = s.split('CDE')
mn = []
for x in range(len(s) - 86):
    ln = 0
    for y in range(0, 86):
        ln += len(s[x + y])
    last = s[x + 86]
    ct = 0
    for y in last:
        if y == 'E':
            ct += 1
        else:
            ct += 1
            break
    if last.count('E') == len(last):
        ct += 1
    mn.append(ln + ct)
print(min(mn) + 87 * 3)
