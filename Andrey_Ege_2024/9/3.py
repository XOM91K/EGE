l = [sorted([int(d) for d in x.split()]) for x in open('3.txt')]
ct = 0
for x in l:
    if x[0] ** 2 * 2 > x[1] * x[2] and x[1] != x[-1] and x[2] != x[-1]:
        if len(set(x)) < len(x):
            ct += 1
print(ct)