import functools , operator, math
l = [sorted([int(d) for d in x.split()]) for x in open('15.txt')]
ct = 0
r = 0
for x in l:
    if len(set(x)) < 7:
        p = [v for v in x if x.count(v) > 1]
        np = sum([v for v in x if x.count(v) == 1])*3
        #r = functools.reduce(operator.mul, p)
        if np <= math.prod(p):
            ct +=1
            print(ct)