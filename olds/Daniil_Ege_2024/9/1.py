l = [sorted([int(d) for d in x.split()]) for x in open('1.txt')]
ct = 0
for x in l:
    if (x[0] + x[-1]) ** 2 > x[1] ** 2 + x[2] ** 2:
        print(x)
        ct += 1
print(ct)
