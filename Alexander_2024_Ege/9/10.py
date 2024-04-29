l = [sorted([int(d) for d in x.split()]) for x in open('10.txt')]
for x in l:
    r = [x.count(y) for y in x]
    if r.count(2) == 4 and r.count(1) == 3:
        if x[-1] != x[-2]:
            print(x, sum(x))