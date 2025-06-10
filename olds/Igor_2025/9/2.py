l = [[int(d) for d in x.split()] for x in open('2.txt')]
ct = 0
for x in l:
    if len(set(x)) == 4:
        x.sort()
        if (x[0] + x[-1]) ** 2 < x[1] ** 2 + x[2] ** 2 + x[3] ** 2:
            ct += 1
print(ct)