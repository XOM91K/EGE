l = [int(x) for x in open('6.txt')]
mx7 = max([y for y in l if str(y)[-1] == '7'])
sr = []
tr = 0
for x in range(len(l) - 2):
    k = 0
    if l[x] % 2 != 0:
        k += 1
    if l[x + 1] % 2 != 0:
        k += 1
    if l[x + 2] % 2 != 0:
        k += 1
    if k == 2:
        d = 0
        if l[x] > mx7:
            d += 1
        if l[x + 1] > mx7:
            d += 1
        if l[x + 2] > mx7:
            d += 1
        if d == 1:
            tr += 1
            sr.append(l[x])
            sr.append(l[x + 1])
            sr.append(l[x + 2])
sr = list(set(sr))
sr = sum(sr) / len(sr)

print(tr, sr)