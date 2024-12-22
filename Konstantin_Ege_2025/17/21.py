l = [int(x) for x in open ('21.txt')]
ct = 0
mx_ch = 0
mn = min([x for x in l if len(str(abs(x))) == 2])
mx_4 = max([x for x in l if len(str(abs(x))) == 4 and abs(x) % 10 == 1])
print(mn, mx_4)
s = []
for x in range(len(l) - 2):
    k = 0
    if l[x] > mn ** 2:
        k += 1
    if l[x + 1] > mn ** 2:
        k += 1
    if l[x + 2] > mn ** 2:
        k += 1
        if k == 2:
            if (abs(l[x]) * abs(l[x + 1]) * abs(l[x + 2])) % mx_4 == 0:
                ct += 1
                s.append(abs(l[x]) + abs(l[x + 1]) + abs(l[x + 2]))
print(ct, max(s))