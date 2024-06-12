l = [[int(d) for d in x.split()] for x in open('9.txt')]
ct = 0
for x in l:
    x.sort()
    if (x[0] + x[-1]) ** 2 > x[1] ** 2 + x[2] ** 2 + x[3] ** 2 + x[4] ** 2 + x[5] ** 2 + x[6] ** 2:
        if len(set(x)) < len(x):
            ct += 1
print(ct)