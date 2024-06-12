l = [int(x) for x in open('1.txt')]
ct = 0
mn = 10**10
for x in range(len(l) - 1):
    if l[x] * l[x + 1] % 2 != 0:
        if ((l[x] + l[x + 1]) / 2) % 7 == 0:
            ct += 1
            mn = min(mn, (l[x] + l[x + 1]) / 2)
print(ct, mn)