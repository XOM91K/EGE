import math
l = [[int(d) for d in x.split()] for x in open('1470.txt')]
for x in l:
    if x[0] < x[1] < x[2] < x[3] < x[4] < x[5] < x[6]:
        if (x[-1] - x[0]) < (x[1] + x[2] + x[3] + x[4] + x[5]):
            print(x, math.prod(x))