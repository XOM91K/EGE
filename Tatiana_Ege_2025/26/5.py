l = [[int(d) for d in x.split()] for x in open('5.txt')]
l = sorted(l, key=lambda d: (-(d[1] + d[2] + d[3]), -d[-1], d[0]))
k = 0
for x in l:
    k += 1
    print(k, x, sum(x[1:-1]))