l = [int(x) for x in open('17.txt')]
sr = [x for x in l if abs(x) % 1000 == 151]
sr = sum(sr) / len(sr)
mn = 10 ** 10
ct = 0
for x in range(len(l) - 2):
    ct4 = 0
    if len(str(abs(l[x]))) == 4:
        ct4 += 1
    if len(str(abs(l[x + 1]))) == 4:
        ct4 += 1
    if len(str(abs(l[x + 2]))) == 4:
        ct4 += 1
    if ct4 == 1 or ct4 == 2:
        ct13 = 0
        ct7 = 0
        if l[x] % 13 == 0:
            ct13 += 1
        if l[x] % 7 == 0:
            ct7 += 1
        if l[x + 1] % 13 == 0:
            ct13 += 1
        if l[x + 1] % 7 == 0:
            ct7 += 1
        if l[x + 2] % 13 == 0:
            ct13 += 1
        if l[x + 2] % 7 == 0:
            ct7 += 1
        if ct13 > ct7:
            if l[x] > sr and l[x + 1] > sr and l[x + 2] > sr:
                ct += 1
                mn = min(mn, l[x] + l[x + 1] + l[x + 2])
print(ct, mn)