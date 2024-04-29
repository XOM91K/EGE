l = [int(x) for x in open('11.txt')]
sr = [x for x in l if str(x)[-3:] == '151']
sr = sum(sr) / len(sr)
ct = 0
mn = 10 ** 10
for x in range(len(l) - 2):
    d13 = 0
    d7 = 0
    g = [len(str(abs(l[x]))), len(str(abs(l[x + 1]))), len(str(abs(l[x + 2])))]
    if g.count(4) > 0 and g.count(4) < 3:
        if l[x] % 13 == 0:
            d13 += 1
        if l[x + 1] % 13 == 0:
            d13 += 1
        if l[x + 2] % 13 == 0:
            d13 += 1
        if l[x] % 7 == 0:
            d7 += 1
        if l[x + 1] % 7 == 0:
            d7 += 1
        if l[x + 2] % 7 == 0:
            d7 += 1
    if d13 > d7 and l[x] > sr and l[x + 1] > sr and l[x + 2] > sr:
        ct += 1
        mn = min(mn, l[x] + l[x + 1] + l[x + 2])
print(ct, mn)
