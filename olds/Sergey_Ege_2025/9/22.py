import math
l = [[int(d) for d in x.split()] for x in open('22.txt')]
c = []
k = 0

for x in l:
    k += 1
    r = []
    if x[0] % 2 == 0:
        r.append('0')
    else:
        r.append('1')
    if x[1] % 2 == 0:
        r.append('0')
    else:
        r.append('1')
    if x[2] % 2 == 0:
        r.append('0')
    else:
        r.append('1')
    if x[3] % 2 == 0:
        r.append('0')
    else:
        r.append('1')
    if x[4] % 2 == 0:
        r.append('0')
    else:
        r.append('1')
    if x[5] % 2 == 0:
        r.append('0')
    else:
        r.append('1')
    if x[6] % 2 == 0:
        r.append('0')
    else:
        r.append('1')
    r = ''.join(r)
    if '11' not in r and '00' not in r:
        povt = []
        nepovt = []
        for y in x:
            if x.count(y) == 1:
                nepovt.append(y)
            else:
                povt.append(y)
        if sum(nepovt) >= math.prod(povt):
            c.append(k)
print(sum(c))