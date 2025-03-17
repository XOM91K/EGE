l = [sorted([int(d) for d in x.split()]) for x in open('6.txt')]
ct = 0
for x in l:
    if x[0] != x[1]:
        if len(set(x)) != 6:
            povt = [y for y in x if x.count(y) > 1]
            if x[0] + x[-1] < sum(povt):
                ct += 1
print(ct)