l = [int(x) for x in open('9.txt')]
M = 10 ** 10
ct = 0
mn = 10 ** 10
mx = 0
for x in l:
    if x % 8 == 0 and x != 8:
        M = min(M, x)
for x in range(len(l) - 1):
    if l[x] % M == 0 and l[x + 1] % M == 0:
        lx = l[x]
        lx1 = l[x + 1]
        if l[x] + l[x + 1] < mn:
            mn = l[x] + l[x + 1]
            mx = max(l[x], l[x + 1])
        ct += 1

print(ct, mx)