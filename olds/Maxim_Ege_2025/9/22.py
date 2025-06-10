l = [sorted([int(d) for d in x.split()]) for x in open('22.txt')]
k = 0
for x in l:
    k += 1
    povt3 = [y for y in x if x.count(y) == 3]
    povt1 = [y for y in x if x.count(y) == 1]
    if len(povt3) == 6 and len(povt1) == 2:
        if (sorted(set(povt3))[-1] - sorted(set(povt3))[0]) ** 2 >= povt1[0] ** 2 + povt1[1] ** 2:
            print(k)
            # 22 44