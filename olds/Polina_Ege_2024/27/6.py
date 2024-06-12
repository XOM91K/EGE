import math
l = [[int(d) for d in x.split()] for x in open('6.txt')]
S = 8244
mn_sm = 10 ** 10
for x in l:
    sm = 0
    for y in l:
        if abs(x[0] - y[0]) > S / 2:
            sm += (S % abs(x[0] - y[0])) * math.ceil(y[1] / 11)
        else:
            sm += abs(x[0] - y[0]) * math.ceil(y[1] / 11)
    mn_sm = min(mn_sm, sm)
print(mn_sm)