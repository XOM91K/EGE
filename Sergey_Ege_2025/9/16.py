l = [sorted([int(d) for d in x.split()]) for x in open('16.txt')]
ct = 0
for x in l:
    if x.count(x[0]) == 1:
        if len(set(x)) != len(x):
            sm = 0
            for y in x:
                if x.count(y) > 1:
                    sm += y
            if x[0] + x[-1] < sm:
                ct += 1
print(ct)