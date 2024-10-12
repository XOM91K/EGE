l = [sorted([int(d) for d in x.split()]) for x in open('7.txt')]
sm = 0
for x in l:
    pt3 = []
    pt2 = []
    for y in x:
        if x.count(y) == 3:
            pt3.append(y)
        if x.count(y) == 2:
            pt2.append(y)
    if len(pt3) == 3 and len(pt2) == 4:
        ch = len([y for y in x[:4] if y % 2 == 0])
        nch = len([y for y in x[:4] if y % 2 == 0])
        if ch == 2 and nch == 2:
            sm += sum(x)
print(sm)