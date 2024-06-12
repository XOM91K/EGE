l = [sorted([int(d) for d in x.split()]) for x in open('13.txt')]
ct = 0
for x in l:
    if len(set(x)) == 6:
        povt = []
        nepovt = []
        for y in x:
            if x.count(y) == 2:
                povt.append(y)
            if x.count(y) == 1:
                nepovt.append(y)
        if nepovt[0] * nepovt[1] * nepovt[2] > povt[0] ** 2:
            ct += 1
print(ct)