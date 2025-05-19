l = [[int(d) for d in x.split()] for x in open('16.txt')]
l = sorted(l, key=lambda d: (-sum(d[1:-1]), -d[-1], d[0]))
ct = 0
for x in l:
    ct += 1
    print(ct, x, sum(x[1:-1]))
#7600410