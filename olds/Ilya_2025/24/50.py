s = open(r'C:\Users\Zarif\Downloads\1483_1.txt').readline()
s = s.split('CDE')
mn_ln = 10 ** 10
for x in range(len(s) - 86):
    ln = 0
    for y in range(0, 86):
        ln += len(s[x + y])
    if len(s[x + 86]) == '':
        ln -= 1
    else:
        for y in s[x + 86]:
            if y == 'E':
                ln += 1
            else:
                ln += 1
                break
        else:
            ln += 1
    mn_ln = min(mn_ln, ln + 3 * 87)
print(mn_ln)