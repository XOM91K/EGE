l = [sorted([int(d) for d in x.split()]) for x in open('13.txt')]
ct = 0
for x in l:
    if len(set(x)) == 6:
        povt = sum(x) - sum(set(x))
        if (x[0] * x[1] * x[2]) > povt ** 2:
            ct += 1
print(ct)