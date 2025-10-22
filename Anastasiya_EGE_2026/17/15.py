l = [int(x) for x in open('15.txt')]
ct = 0
ok7 = max([x for x in l if str(x)[-1] == '7'])
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
        k = 0
        if l[x] > ok7:
            k += 1
        if l[x + 1] > ok7:
            k += 1
        if l[x + 2] > ok7:
            k += 1
        if k == 1:
            ct += 1
            sr.append(l[x])
            sr.append(l[x + 1])
            sr.append(l[x + 2])
d = list(set(sr))
print(ct, sum(d) / len(d))
