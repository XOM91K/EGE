s = open(r'C:\Users\Zarif\Downloads\1397_2.txt').readline()
s = s.split('RSQ')
mn_ln = 10 ** 10
for x in range(len(s) - 129):
    ln = 0
    for y in range(129):
        ln += len(s[x + y])
    for y in s[x + 129]:
        if y == 'Q':
            ln += 1
        else:
            ln += 1
            break
    else:
        ln += 1
    mn_ln = min(mn_ln, ln + 3 * 130)
print(mn_ln)