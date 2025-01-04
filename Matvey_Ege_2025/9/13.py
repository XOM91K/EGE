l = [sorted([int(d) for d in x.split()]) for x in open('13.txt')]
ct = 0
for x in l:
    c = list(set(x))
    e = []
    if len(c) == 3:
        for i in c:
            e.append(x.count(i))
        if e.count(2) == 2 and e.count(3) == 1:
            #if (x[-1] + x[-3]) % 2 != 0 and (x[-2] + x[-4]) % 2 != 0:
            ee = []
            c = x[:4]
            for i in c:
                ee.append(1 if i % 2 == 1 else 0)
            if ee.count(1) == 2 and ee.count(0) == 2:
                ct += sum(x)
print(ct)