l = [sorted([int(d) for d in x.split()]) for x in open('4.txt')]
ct = 0
for x in l:
    if x.count(x[0]) == 1:
        if len(set(x)) < len(x):
            povt = []
            for y in x:
                if x.count(y) > 1:
                    povt.append(y)
            if (x[0] + x[-1]) < sum(povt):
                ct += 1
print(ct)