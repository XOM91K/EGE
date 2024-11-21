import math
#Жиесть
l = [[int(d) for d in x.split()] for x in open('16.txt')]
ct = 0
k = 0
for x in l:
    k += 1
    d = x.copy()
    #четные t нечётные  m
    if d[0] % 2 == 0:
        d[0] = 't'
    else:
        d[0] = 'm'
    if d[1] % 2 == 0:
        d[1] = 't'
    else:
        d[1] = 'm'
    if d[2] % 2 == 0:
        d[2] = 't'
    else:
        d[2] = 'm'
    if d[3] % 2 == 0:
        d[3] = 't'
    else:
        d[3] = 'm'
    if d[4] % 2 == 0:
        d[4] = 't'
    else:
        d[4] = 'm'
    if d[5] % 2 == 0:
        d[5] = 't'
    else:
        d[5] = 'm'
    if d[6] % 2 == 0:
        d[6] = 't'
    else:
        d[6] = 'm'
    d = ''.join(d)
    if 'tt' not in d and 'mm' not in d:
        povt = []
        nepovt = []
        for y in x:
            if x.count(y) > 1:
                povt.append(y)
            if x.count(y) == 1:
                nepovt.append(y)
        if sum(nepovt) * 3 >= math.prod(povt):
            ct += k
print(ct)