l = [sorted([int(d) for d in x.split()]) for x in open('5.txt')]
ct = 0
for x in l:
    if x[0] != x[1]:
        if len(set(x)) < 6:
            sm_povt = 0
            for y in range(0, 6):
                if x.count(x[y]) > 1:
                    sm_povt = sm_povt + x[y]
            if (x[0] + x[-1]) < sm_povt:
                ct += 1
print(ct)