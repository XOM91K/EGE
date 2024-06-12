l = [int(x) for x in open('15.txt')]
mx3 = sorted(l)[-3]
ct = 0
mx = 0
for x in range(len(l) - 2):
    k = 0
    if l[x] % 2 == 0:
        k += 1
    if l[x + 1] % 2 == 0:
        k += 1
    if l[x + 2] % 2 == 0:
        k += 1
    if k <= 2:
        if (l[x] + l[x + 1] + l[x + 2]) <= mx3:
            ct += 1
            mx = max(mx, l[x] + l[x + 1] + l[x + 2])
print(ct, mx)