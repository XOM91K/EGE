l = [[int(d) for d in x.split()] for x in open('18.txt')]
for x in l:
    povt3 = [y ** 2 for y in x if x.count(y) == 3]
    ost = [y for y in x if x.count(y) != 3]
    if len(povt3) > 0:
        if sum(povt3) >= sum(ost) ** 2:
            print(sum(x))