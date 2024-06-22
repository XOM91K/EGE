l = [sorted([int(d) for d in x.split()]) for x in open('6.txt')]
ct = 0
for x in l:
    if len(set(x)) == 3:
        if x[-1] % x[0] != 0:
            if x[-1] + x[-2] > 2 * (x[0] + x[1]):
                ct += 1
print(ct)