l = [sorted([int(d) for d in x.split()]) for x in open('2.txt')]
sm = 0
for x in l:
    ct3 = 0
    ct2 = 0
    for y in x:
        if x.count(y) == 3:
            ct3 += 1
        if x.count(y) == 2:
            ct2 += 1
    if ct3 == 3 and ct2 == 4:
        if (x[0] % 2 == 0 and x[2] % 2 != 0) or (x[0] % 2 != 0 and x[2] % 2 == 0):
            sm += sum(x)
print(sm)