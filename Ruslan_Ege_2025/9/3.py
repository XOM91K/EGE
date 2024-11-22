l = [sorted([int(d) for d in x.split()]) for x in open('3.txt')]
sm = 0
for x in l:
    # [26, 26, 26, 11, 11, 12, 12]
    # [1, 1, 1, 1, 1, 2, 3]
    povt3 = []
    povt2 = []
    for y in x:
        if x.count(y) == 3:
            povt3.append(y)
        if x.count(y) == 2:
            povt2.append(y)
    if len(povt3) == 3 and len(povt2) == 4:
        d = x[:4]
        ct_ch = len([f for f in d if f % 2 == 0])
        if ct_ch == 2:
            sm += sum(x)
print(sm)