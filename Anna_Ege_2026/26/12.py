l = [[int(d) for d in x.split()] for x in open('12.txt')]
sm = [200, 200, 200, 200]
inds = [0, 0, 0, 0]

for x in range(4):
    tovar = 0
    while sm[x] + tovar > 0:
        mn = 10 ** 10
        ind = -1
        for xx in range(len(inds)):
            if mn < min(l[x][inds[xx]:]):
                mn = min(l[xx:])
                ind = xx
        inds[ind] += 1
        tovar = mn
        sm[x] -= mn

print(l)