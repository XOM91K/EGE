l = [int(x) for x in open('1.txt')]
sr = [d for d in l if abs(d) % 1000 == 151]
sr = sum(sr) / len(sr)
ct = 0
mn = 100_000
for x in range(len(l) - 2):
    ln = [len(str(abs(l[x]))), len(str(abs(l[x + 1]))), len(str(abs(l[x + 2])))]
    if 4 in ln and ln.count(4) != 3:
        g13 = 0
        g7 = 0
        if l[x] % 13 == 0:
            g13 += 1
        if l[x + 1] % 13 == 0:
            g13 += 1
        if l[x + 2] % 13 == 0:
            g13 += 1

        if l[x] % 7 == 0:
            g7 += 1
        if l[x + 1] % 7 == 0:
            g7 += 1
        if l[x + 2] % 7 == 0:
            g7 += 1
        if g13 > g7:
            if l[x] > sr and l[x + 2] > sr and l[x + 1] > sr:
                ct += 1
                mn = min(mn, l[x] + l[x + 1] + l[x + 2])
print(ct, mn)