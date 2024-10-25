import math
l = [x.split() for x in open('input.txt')]
l = sorted(l, key=lambda d: d[0].split('.')[1])
ed_izm = ['B', 'KB', 'MB', 'GB', 'TB']
dt = {}
for x in l:
    if x[0].split('.')[1] not in dt:
        dt[x[0].split('.')[1]] = []
    dt[x[0].split('.')[1]].append(x)
print(dt)
for x in dt:
    for y in dt[x]:
        print(y[0])
    print('----------')
    max_ed_izm = max([ed_izm.index(d[-1]) for d in dt[x]])
    sm = 0
    for y in dt[x]:
        sm += int(y[1]) / (1024 ** (max_ed_izm - ed_izm.index(y[2])))
    sm = math.ceil(sm)
    print('Summary:', sm, ed_izm[max_ed_izm])
    print()