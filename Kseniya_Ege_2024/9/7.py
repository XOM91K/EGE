l = [[int(d) for d in x.split()] for x in open('7.txt')]
for x in l:
    ct4 = 0
    ct2 = 0
    ct1 = 1
    for y in x:
        if x.count(y) == 4:
            ct4 += 1
        if x.count(y) == 2:
            ct2 += 1
        if x.count(y) == 1:
            ct1 += 1
    if ct4 == 4 and ct2 == 2 and ct1 == 3:
        print(x)