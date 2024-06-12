#5437
l = [int(x) for x in open('2.txt')]
ct = 0
mn = 10**10
for x in range(len(l) - 2):
    tr1 = str(l[x])[::-1]
    tr2 = str(l[x + 1])[::-1]
    tr3 = str(l[x + 2])[::-1]
    sm1 = 0
    sm11 = 0
    for y in range(len(tr1)):
        if y % 2 != 0:
            sm1 += int(tr1[y])
        else:
            sm11 += int(tr1[y])
    sm2 = 0
    sm22 = 0
    for y in range(len(tr2)):
        if y % 2 != 0:
            sm2 += int(tr2[y])
        else:
            sm22 += int(tr2[y])
    sm3 = 0
    sm33 = 0
    for y in range(len(tr3)):
        if y % 2 != 0:
            sm3 += int(tr3[y])
        else:
            sm33 += int(tr3[y])
    if sm11 != 0 and sm22 != 0 and sm33 != 0 and sm1 % sm11 == 0 and sm2 % sm22 == 0 and sm3 % sm33 == 0:
        ct += 1
        mn = min(mn, l[x] + l[x + 1] + l[x + 2])
print(ct, mn)