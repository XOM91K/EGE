l = [sorted([int(d) for d in x.split()]) for x in open('1.txt')]
ct = 0
for x in l:
    if x[0] != x[1]:
        if len(set(x[1:])) < 5:
            r = []
            for y in x:
                if x.count(y) > 1:
                    r.append(y)
            if (max(x) + min(x)) < sum(r):
                ct += 1
print(ct)