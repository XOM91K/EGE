l = [int(x) for x in open('10.txt')]
mx = 0
ct = 0
mx_sm = 0
for x in l:
    d = x
    s = ''
    while d > 0:
        s += str(d % 6)
        d //= 6
    s = s[::-1]
    if s[-2:] == '23':
        mx = max(mx, x)
for x in range(len(l) - 2):
    if (len(str(abs(l[x]))) == 4 and len(str(abs(l[x + 1]))) != 4 and len(str(abs(l[x + 2]))) != 4) or \
        (len(str(abs(l[x]))) != 4 and len(str(abs(l[x + 1]))) == 4 and len(str(abs(l[x + 2]))) != 4) or \
            (len(str(abs(l[x]))) != 4 and len(str(abs(l[x + 1]))) != 4 and len(str(abs(l[x + 2]))) == 4):
        if (l[x] + l[x + 1] + l[x + 2]) % mx == 0:
            ct += 1
            mx_sm = max(mx_sm, l[x] + l[x + 1] + l[x + 2])
print(ct, mx_sm)
