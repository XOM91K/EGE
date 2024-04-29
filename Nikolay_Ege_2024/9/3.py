l = [[int(d) for d in x.split()] for x in open('3.txt')]
ct = 0
for x in l:
    povt = []
    for y in x:
        if x.count(y) == 2:
            povt.append(y)
    if len(povt) == 6:
        x = sorted(set(x))
        if x[-1] ** 2 == x[0] ** 2 + x[1] ** 2:
            ct += 1
print(ct)