l = [sorted([int(d) for d in x.split()]) for x in open('12.txt')]
ct = 0
for x in l:#[33, 33, 33, 35, 37, 39, 40]
    povt = (sum(x) - sum(set(x))) // 2
    if len(set(x)) == 5 and (x.count(x[2]) == 3 or x.count(x[4]) == 3):
        if (sum(x) - povt * 3) / 4 < povt:
            ct += 1
print(ct)