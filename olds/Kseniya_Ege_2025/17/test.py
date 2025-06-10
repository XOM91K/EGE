l = [int(x) for x in open('test.txt')]
mx = max([x for x in l if str(x)[-1] == '7'])
mr_ee = []
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
        s = 0
        if l[x] > mx:
            s += 1
        if l[x + 1] > mx:
            s += 1
        if l[x + 2] > mx:
            s += 1
        if s == 1:
            mr_ee.append(l[x])
            mr_ee.append(l[x + 1])
            mr_ee.append(l[x + 2])
            ct += 1
print(mr_ee)
print(len(mr_ee) / 3)
#print(ct, sum(set(mr_ee)) / len(set(mr_ee)))