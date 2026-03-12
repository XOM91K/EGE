l = [[int(d) for d in x.split()] for x in open('16.txt')]
l = sorted(l, key=lambda d: (-(d[1] + d[2] + d[3]), -d[-1], d[0]))
k = 0
for x in l:
    k += 1
    print(k, x, x[1] + x[2] + x[3])