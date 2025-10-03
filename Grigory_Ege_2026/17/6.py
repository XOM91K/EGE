l = [int(x) for x in open('6.txt')]
sr = []
ct = 0
mx7 = max([x for x in l if str(x)[-1] == '7'])
for x in range(len(l) - 2):
    k = 0
    if l[x] % 2 != 0:
        k += 1
    if l[x + 1] % 2 != 0:
        k += 1
    if l[x + 2] % 2 != 0:
        k += 1
    if k == 2:
        k = 0
        if l[x] > mx7:
            k += 1
        if l[x + 1] > mx7:
            k += 1
        if l[x + 2] > mx7:
            k += 1
        if k == 1:
            sr.append(l[x])
            sr.append(l[x +1])
            sr.append(l[x + 2])
            ct += 1
print(ct, sum(set(sr)) / len(set(sr)))