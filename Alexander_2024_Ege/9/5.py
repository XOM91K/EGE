l = [sorted([int(d) for d in x.split()]) for x in open('5.txt')]
ct = 0
for x in l:
    if (x.count(x[2]) == 3 or x.count(x[4]) == 3) and len(set(x)) == 5:
        d3 = (sum(x) - sum(set(x))) // 2
        if (sum(x) - d3 * 3) / 4 <= d3:
            ct += 1
print(ct)