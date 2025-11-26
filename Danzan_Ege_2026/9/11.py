import math
l = [[int(d) for d in x.split()]for x in open('11.txt')]
k = 0
sm = 0
for x in l:
    k+=1
    if x[0]%2 != x[1]%2 and x[1]%2 != x[2]%2 and x[2]%2 != x[3]%2 and x[3]%2 != x[4]%2 and x[4]%2 != x[5]%2 and x[5]%2 != x[6]%2:
        y = [d for d in x if x.count(d) > 1] # []
        y2 = [d for d in x if x.count(d) == 1]
        # pr = 1
        # for d in y:
        #     pr *= d
        # print(pr, math.prod(y))
        if sum(y2)*3 >= math.prod(y):
            sm += k

print(sm)