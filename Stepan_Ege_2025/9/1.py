l = [sorted([int(d) for d in x.split()]) for x in open('1.txt')]
ct = 0
for x in l:
    if len(set(x)) == 5:
        if (x[-1] + x[0]) / 2 > (x[1] + x[2] + x[3] + x[4]) / 4:
            ct += 1
print(ct)