l = [sorted([int(d) for d in x.split()]) for x in open('10.txt')]
ct = 0
sm = 0
for x in l:
    tr = []
    dv = []
    for y in x:
        if x.count(y) == 3:
            tr.append(y)
        elif x.count(y) == 2:
            dv.append(y)
    if len(tr) == 3 and len(dv) == 4:
        ch = 0
        nch = 0
        for y in x[:4]:
            if y % 2 == 0:
                ch += 1
            else:
                nch += 1
        if not(ch >= 3 or nch >= 3):
            sm += sum(x)
print(sm)