l = [sorted([int(d) for d in g.split()]) for g in open('11.txt')]
ct = 0
for x in l:
    # [1, 1, 1, 3, 4, 5]
    if len(set(x))== 4 and (x.count(x[2]) == 3 or x.count(x[3]) == 3):
        povt = []
        nepovt = []
        for y in x:
            if x.count(y) == 1:
                nepovt.append(y)
            if x.count(y) >= 2:
                povt.append(y)
        if sum(nepovt) / 3 < sum(povt):
            ct += 1
print(ct)
