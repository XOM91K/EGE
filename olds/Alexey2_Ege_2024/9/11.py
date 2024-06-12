l = [sorted([int(d) for d in x.split()]) for x in open('11.txt')]
ct = 0
n = 0
for x in l:
    k = 0
    if (x[0] + x[-1]) ** 2 > x[1] ** 2 + x[2] ** 2 + x[3] ** 2 + x[4] ** 2:
        k += 1
    if (len(set(x)) == 4 and (x.count(x[2]) == 3 or x.count(x[3]) == 3 or x.count(x[4]) == 3)):
        k += 1
    if k > 0:
        ct += 1
print(ct)