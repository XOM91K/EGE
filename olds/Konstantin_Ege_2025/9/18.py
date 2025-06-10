l = [sorted([int(d) for d in x.split()]) for x in open('18.txt')]
ct = 0
for x in l:
    if (x[3] + x[4]) * 2 > (x[0] + x[1] + x[2]) * 3:
        g = [f for f in x if f % 10 == 5]
        if len(g) >= 2:
            ct += 1
print(ct)