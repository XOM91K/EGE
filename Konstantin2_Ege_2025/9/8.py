l = [sorted([int(d) for d in x.split()]) for x in open('8.txt')]
ct = 0
for x in l:
    if x.count(x[0]) == 1:
        if len(set(x)) <= 5:
            pvt = 0
            for y in range(len(x)):
                if x.count(x[y]) > 1:
                    pvt += x[y]
            if (x[0] + x[-1]) < pvt:
                ct += 1
                print(x)
print(ct)