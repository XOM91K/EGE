import math
l = [[int(d) for d in x.split()] for x in open('14.txt')]
k = 0
sm = 0
for x in l:
    k = k + 1
    if x[0] % 2 != x[1] % 2 and x[1] % 2 != x[2] % 2 and x[2] % 2 != x[3] % 2 and x[3] % 2 != x[4] % 2 and x[4] % 2 != x[5] % 2 and x[5] % 2 != x[6] % 2:
        pov = []
        nepov = []
        for y in x:
            if x.count(y) > 1:
                pov.append(y)
            if x.count(y) == 1:
                nepov.append(y)
        if 3 * sum(nepov) >= math.prod(pov):
            print(k, x)
            sm += k
print(sm)