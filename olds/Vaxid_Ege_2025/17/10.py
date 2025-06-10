l = [int(x) for x in open('10.txt')]
mx = max([d for d in l if str(d)[-1] == '7'])
ct = 0
sr = []
for x in range(len(l) - 2):
    k = 0
    if l[x] % 2 != 0:
        k += 1
    if l[x + 1] % 2 != 0:
        k += 1
    if l[x + 2] % 2 != 0:
        k += 1
    if k == 2:
        q = 0
        if l[x] > mx:
            q += 1
        if l[x + 1] > mx:
            q += 1
        if l[x + 2] > mx:
            q += 1
        if q == 1:
            ct += 1
            sr.append(l[x])
            sr.append(l[x + 1])
            sr.append(l[x + 2])
sr = sum(list(set(sr))) / len(list(set(sr)))
print(ct)
print(sr)