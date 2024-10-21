l = [sorted([int(d) for d in x.split()]) for x in open('14.txt')]
sm = 0
for x in l:
    povt3 = []
    povt2 = []
    for y in x:
        if x.count(y) == 3:
            povt3.append(y)
        if x.count(y) == 2:
            povt2.append(y)
    if len(povt3) == 3 and len(povt2) == 4:
        if (x[0] % 2 == 0 and x[2] % 2 != 0) or (x[0] % 2 != 0 and x[2] % 2 == 0):
            sm += sum(x)
print(sm)