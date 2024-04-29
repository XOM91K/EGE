l = [sorted([int(d) for d in x.split()]) for x in open('4.txt')]
ct = 0
for x in l:
    if len(set(x)) < len(x):
        if x[0] ** 2 * 2 > x[1] * x[2] and x[1] != x[3] and x[2] != x[3]:
            ct += 1
print(ct)