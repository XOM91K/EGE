s = open('24.txt').readline().split('RSQ')
mn_ln = 10 ** 10
for x in range(len(s) - 129):
    ln = 0
    for y in range(0, 130):
        ln += len(s[x + y])
    last = s[x + y]
    k = 0
    for word in last:
        if word == 'Q':
            k += 1
        else:
            k += 1
            break
    else:
        k += 1
    mn_ln = min(mn_ln, ln + k + (130 * 3))
print(mn_ln)