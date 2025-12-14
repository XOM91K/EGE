s = open(r'C:\Users\Zarif\Downloads\1397_2 (10).txt').readline()
s = s.split('RSQ')
mn = []
for x in range(len(s) - 129):
    ln = 0
    for y in range(0, 129):
        ln += len(s[x + y])
    ct = 0
    for y in s[x + 129]:
        if y == 'Q':
            ct += 1
        else:
            ct += 1
            break
    else:
        ct += 1
    mn.append(ct + ln + 3 * 130)
print(min(mn))