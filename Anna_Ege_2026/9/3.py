l = [[int(d) for d in x.split()] for x in open('3.txt')]
ct = 0
for x in l:
    if len(set(x)) == 6:
        x.sort()
        if (x[0] + x[-1]) / 2 < (x[1] + x[2] + x[3] + x[4]) / 4:
            ct += 1
print(ct)