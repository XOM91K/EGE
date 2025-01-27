l = [int(x) for x in open ('23.txt')]
mx_ch = max([x for x in l if x % 10 == 7])
print(mx_ch)
s = []
ct = 0
for x in range(len(l) - 1):
    if (str(l[x])[0]) == (str(l[x + 1])[0]):
        f = 0
        if l[x] % 10 == 7 and len(str(l[x])) == 3:
            f += 1
        if l[x + 1] % 10 == 7 and len(str(l[x + 1])) == 3:
            f += 1
        if f >= 1:
            if (l[x] + l[x + 1]) < mx_ch:
                ct += 1
                s.append(l[x] + l[x + 1])
print(ct, max(s))