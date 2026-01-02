s = open(r'C:\Users\Zarif\Downloads\1483_1 (8).txt').readline()
s = s.split('CDE')
mx = []
for x in range(len(s) - 86):
    ln = ''
    for y in range(0, 86):
        ln += s[x + y] + 'CDE'
    ln = ln[:-3]
    for y in s[x + 86]:
        if y != 'E':
            ln += y
        else:
            ln += y
            break
    else:
        ln += 'C'
    mx.append(ln)
print(len(min(mx, key=len)) + 3 * 87)