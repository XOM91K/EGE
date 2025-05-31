l = [[int(d) for d in x.split()] for x in open('11.txt')]
for x in l:
    ct = [x.count(y) for y in x]
    if ct.count(3) >= 1:
        pvt = [y ** 2 for y in x if x.count(y) == 3]
        npvt = [y for y in x if x.count(y) == 1]
        if sum(pvt) >= sum(npvt) ** 2:
            print(sum(x))