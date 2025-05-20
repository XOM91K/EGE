l = [int(x) for x in open('11.txt')]
mx7 = max([x for x in l if str(x)[-1] == '7'])
sr = []
ct = 0
for x in range(len(l) - 2):
    k = 0
    if l[x] % 2 != 0:
        k += 1
    if l[x + 1] % 2 != 0:
        k += 1
    if l[x + 2] % 2 != 0:
        k += 1
    if k == 2:
        n = 0
        if l[x] > mx7:
            n += 1
        if l[x + 1] > mx7:
            n += 1
        if l[x + 2] > mx7:
            n += 1
        if n == 1:
            ct += 1
            sr.append(l[x])
            sr.append(l[x + 1])
            sr.append(l[x + 2])
sr = set(sr)
print(sum(sr) / len(sr))
print(ct)