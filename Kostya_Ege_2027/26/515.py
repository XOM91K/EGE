l = [[int(d) for d in x.split()] for x in open('515.txt')]
l = sorted(l, key=lambda d: (-sum(d[1:-1]), -d[-1], d[0]))
k = 0
for x in l:
    k += 1
    print(k, x, sum(x[1:-1]))