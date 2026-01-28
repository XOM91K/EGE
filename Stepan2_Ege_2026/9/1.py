l = [[int(d) for d in x.split()] for x in open('1.txt')]
ct = 0
for x in l:
    povt2 = [d for d in x if x.count(d) == 2]
    povt1 = [d for d in x if x.count(d) == 1]
    if len(povt2) == 2 and len(povt1) == 3:
        x = sorted(x)
        if (x[0] + x[4]) ** 2 < x[1] ** 2 + x[2] ** 2 + x[3] ** 2:
            ct += 1
print(ct)