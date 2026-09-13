import math
l = [[int(d) for d in x.split()] for x in open('438.txt')]
k = 0
sm = 0
for x in l:
    k += 1
    if x[0] % 2 != x[1] % 2 and x[1] % 2 != x[2] % 2 and x[2] % 2 != x[3] % 2 and x[3] % 2 != x[4] % 2 and x[4] % 2 != x[5] % 2 and x[5] % 2 != x[6] % 2:
        nepov = [d for d in x if x.count(d) == 1]
        pov = [d for d in x if x.count(d) > 1]
        if 3 * sum(nepov) >= math.prod(pov):
            sm += k
print(sm)