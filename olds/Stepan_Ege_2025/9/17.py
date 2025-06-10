l = [sorted([int(d) for d in x.split()]) for x in open('17.txt')]
ct = 0
for x in l:
    if len(set(x)) == 4 and x.count(x[2]) != 3 and x.count(x[3]) != 3:
        povt = []
        nepovt = []
        for y in x:
            if x.count(y) > 1:
                povt.append(y)
            if x.count(y) == 1:
                nepovt.append(y) # [22, 11, 39, 22]
        if max(povt) ** 2 > nepovt[0] * nepovt[1]:
            ct += 1
print(ct)