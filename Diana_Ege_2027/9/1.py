l = [[int(d) for d in x.split()] for x in open('1.txt')]
ct = 0
for x in l:
    povt2 = [k for k in x if x.count(k) == 2]
    povt1 = [k for k in x if x.count(k) == 1]
    if len(povt2) == 2 and len(povt1) == 3:
        x = sorted(x)
        if (x[0] + x[-1]) ** 2 < x[1] ** 2 + x[2] ** 2 + x[3] ** 2:
            print(x)
            ct += 1
print(ct)