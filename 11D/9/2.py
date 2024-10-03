l = [sorted([int(d) for d in x.split()]) for x in open('2.txt')]
sm = 0
for x in l:
    povt3 = []
    povt2 = []
    for y in x:
        if x.count(y) == 2:
            povt2.append(y)
        if x.count(y) == 3:
            povt3.append(y)
    if len(povt3) == 3 and len(povt2) == 4:
        print(x)
        ch = 0
        nch = 0
        for y in x[:4]:
            if y % 2 == 0:
                ch += 1
            else:
                nch += 1
        if ch == 2 and nch == 2:
            sm += sum(x)
print(sm)