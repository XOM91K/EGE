l = [sorted([int(d) for d in x.split()]) for x in open('1.txt')]
k = 0
for x in l:
    if (x[0] + x[-1]) ** 2 > x[1] ** 2 + x[2] ** 2 + x[3] ** 2:
        k += 1
print(k)