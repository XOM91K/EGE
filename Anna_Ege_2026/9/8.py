import math
l = [[int(d) for d in x.split()]for x in open('8.txt')]
k = 0
for x in l:
    k += 1
    if x[0] < x[1] < x[2] < x[3] < x[4] < x[5] < x[6]:
        x = sorted(x)
        if x[-1] - x[0] < (x[1] + x[2] + x[3] + x[4] + x[5]):
            print(k, *x, math.prod(x))
            break