l = [sorted([int(d) for d in x.split()]) for x in open('7.txt')]
ct = 0
for x in l:
    if x.count(x[0]) == 1 and len(set(x)) <= 5 and (x[0] + x[-1]) < ((x[1] + x[2] + x[3] + x[4]) / 4) * 2:
        ct = ct + 1
print(ct)