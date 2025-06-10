l = [int(x) for x in open('24.txt')]
ct = 0
minu = 10 ** 10
mx_ch = max([x for x in l if x % 10 == 1])
for x in range(len(l) - 3):
    a = 0
    if l[x] % 2 == 0:
        a += 1
    if l[x + 1] % 2 == 0:
        a += 1
    if l[x + 2] % 2 == 0:
        a += 1
    if l[x + 3] % 2 == 0:
        a += 1
    if a % 2 != 0:
        j = 0
        if l[x] < mx_ch:
            j += 1
        if l[x + 1] < mx_ch:
            j += 1
        if l[x + 2] < mx_ch:
            j += 1
        if l[x + 3] < mx_ch:
            j += 1
        if j == 4:
            ct += 1
            minu = min(minu, (l[x]) + (l[x + 1]) + (l[x + 2]) + (l[x + 3]))
print(ct, minu)