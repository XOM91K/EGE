l = [sorted([int(d) for d in x.split()]) for x in open('2.txt')]
ct = 0
for x in l:
    # x = [22, 33, 22, 22, 4, 5]
    # [22, 33, 4, 5]
    if x.count(min(x)) == 1:
        if len(set(x)) < 6:
            if (x[0] + x[-1]) < 2 * ((x[1] + x[2] + x[3] + x[4]) / 4):
                ct += 1
print(ct)
