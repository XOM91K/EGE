l =[sorted([int(d) for d in x.split()]) for x in open('11.txt')]
ct =0
for x in l:
    if x[0] != x[1]:
        povt = []
        for y in x[1:]:
            if x[1:].count(y) > 1:
                povt.append(y)
        if len(povt) > 0:
            if x[0] + x[-1] < (x[1] + x[2] + x[3] + x[4]) / 4 * 2:
                ct += 1
print(ct)