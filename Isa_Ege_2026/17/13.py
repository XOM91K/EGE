l = [int(d) for d in open('13.txt')]
mx = []
nx = []
ct = 0
for x in range(len(l) - 2):
    k = 0
    if l[x] % 40 == 15:
        k += 1
    if l[x + 1] % 40 == 15:
        k += 1
    if l[x + 2] % 40 == 15:
        k += 1
    if k == 2:
        m = 0
        if l[x] % 7 == 0:
            m += 1
        if l[x + 1] % 7 == 0:
            m += 1
        if l[x + 2] % 7 == 0:
            m += 1
        if m <= 2:
            ct += 1
            mx.append(l[x])
            mx.append(l[x + 1])
            mx.append(l[x + 2])
print(ct, sum(x for x in mx if x % 40 != 15))
