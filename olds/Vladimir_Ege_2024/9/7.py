l = [sorted([int(d) for d in x.split()]) for x in open('7.txt')]
for x in l:
    # 11, 18, 18, 64, 64, 74, 95
    if x[-1] != x[-2]:
        povt = []
        nepovt = []
        for y in x:
            if x.count(y) == 2:
                povt.append(y)
            if x.count(y) == 1:
                nepovt.append(y)
        if len(nepovt) == 3 and len(povt) == 4:
            print(sum(x))