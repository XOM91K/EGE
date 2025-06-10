l = [sorted([int(d) for d in x.split()]) for x in open('6.txt')]
ct = 0
for x in l:
    if len(x) == len(set(x)):
        if (x[0] + x[-1]) / 2 == x[2] == (x[1] + x[3]) / 2:
            ct += 1
print(ct)