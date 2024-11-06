import math
cnt = 0
sm = 0
sm_num = 0
l = [[int(d) for d in x.split()] for x in open("8.txt")]
for x in l:
    sm_num += 1
    can = True
    for y in range(len(x) - 1):
        if x[y] % 2 == x[y+1] % 2:
            can = False
    if can:
        pvtr = [int(y) for y in x if x.count(y) > 1]
        nepvtr = [int(y) for y in x if x.count(y) == 1]
        pr_pvtr = math.prod(pvtr)
        if len(pvtr) == 0:
            pr_pvtr = 0
        if 3*sum(nepvtr) >= pr_pvtr:
            sm += sm_num
print(sm)