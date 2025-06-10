l = [sorted([int(d) for d in x.split()]) for x in open('13.txt')]
ct = 0
for x in l:
    # [22, 22, 22, 1, 2, 3]

    povt = [y for y in x if x.count(y) == 3]
    nepovt = [y for y in x if x.count(y) == 1]
    if len(povt) == 3 and len(nepovt)==3:
        if (sum(povt))**2 > (sum(nepovt))**2:
            ct += 1
print(ct)