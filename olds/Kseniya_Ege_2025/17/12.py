l = [int(x) for x in open('12.txt')]
mn = []
sr = [x for x in l if str(x)[-3:] == '151']
sr = sum(sr) / len(sr)
print(sr)
for x in range(len(l) - 2):
    k = 0
    if len(str(abs(l[x]))) == 4:
        k += 1
    if len(str(abs(l[x + 1]))) == 4:
        k += 1
    if len(str(abs(l[x + 2]))) == 4:
        k += 1
    if 1 <= k <= 2:
        dl = [] # 13
        ds = [] # 7
        if l[x] % 13 ==0:
            dl.append(l[x])
        if l[x + 1] % 13 == 0:
            dl.append(l[x + 1])
        if l[x + 2] % 13 == 0:
            dl.append(l[x + 2])
        if l[x] % 7 == 0:
            ds.append(l[x])
        if l[x + 1] % 7 == 0:
            ds.append(l[x + 1])
        if l[x + 2] % 7 == 0:
            ds.append(l[x + 2])
        if  len(dl) > len(ds):
                if l[x] > sr and l[x + 1] > sr and l[x + 2] > sr:
                    mn.append(l[x] + l[x + 1] + l[x + 2])
print(len(mn), min(mn))