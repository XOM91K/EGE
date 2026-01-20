def dels(d):
    l = []
    for x in range(1, int(d ** 0.5) + 1):
        if d % x == 0:
            l.append(x)
            l.append(d // x)
    return sorted(set(l))
for x in range(10_000, 31623):
    x = x ** 2
    l = dels(x)
    if len(l) == 39 and x % 2 == 0:
        print(x, max([d for d in l if d % 2 != 0]))
100962304 24649
108826624 26569
114233344 27889
122589184 29929
131239936 32041
893292544 218089
939790336 229441
971444224 237169
976562500 244140625
987467776 241081


import math
k=0
sm=0
l=[[int(d) for d in x.split()] for x in open('19.txt')]
for x in l:
    k+=1
    nepovt = [d for d in x if x.count(d) == 1]
    povt = [m for m in x if x.count(m)>1]
    if sum(nepovt) * 3 >= math.prod(povt):
        if (x[0]%2==0 and x[1]%2==1 and x[2]%2==0 and x[3]%2==1 and x[4]%2==0 and x[5]%2==1 and x[6]%2==0) or (x[0]%2==1 and x[1]%2==0 and x[2]%2==1 and x[3]%2==0 and x[4]%2==1 and x[5]%2==0 and x[6]%2==1):

            sm+=k
            print(x)
print(sm)