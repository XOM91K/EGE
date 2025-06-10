l = [sorted([int(d) for d in x.split()]) for x in open('14.txt')]
sm = 0
for x in l:
    # 10, 10, 10, 44, 44, 99, 99
    povt3 = []
    povt2 = []
    for y in x:
        if x.count(y) == 3:
            povt3.append(y)
        if x.count(y) == 2:
            povt2.append(y)
    if len(povt3) == 3 and len(povt2) == 4:
        ch = 0
        nch = 0
        if x[0] % 2 == 0:
            ch += 1
        else:
            nch += 1
        if x[1] % 2 == 0:
            ch += 1
        else:
            nch += 1
        if x[2] % 2 == 0:
            ch += 1
        else:
            nch += 1
        if x[3] % 2 == 0:
            ch += 1
        else:
            nch += 1
        if ch == 2 and nch == 2:
            sm += sum(x)
print(sm)