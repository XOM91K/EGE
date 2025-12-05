import re
s = open(r'C:\Users\Zarif\Downloads\1397_2 (9).txt').readline()
s = s.split('RSQ')
mn = []
mn2 = 10 ** 10
for x in range(len(s) - 129):
    ln = 0
    for y in range(129):
        ln += len(s[x + y])
    s2 = s[x + 129]
    ct = 1
    for y in s2:
        if y == 'Q':
            ct += 1
        else:
            break
    mn2 = min(mn2, ln + ct)
print(mn2)