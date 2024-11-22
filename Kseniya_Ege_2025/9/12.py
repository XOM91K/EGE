l = [sorted([int(d) for d in x.split()]) for x in open('12.txt')]
ct = 0
for x in l:
    if x[0] != x[1]:
        if len(set(x[1:])) < 5:
            if x[0] + x[-1] < (x[1] + x[2] + x[3] + x[4]) / 4 * 2:
                ct += 1
print(ct)