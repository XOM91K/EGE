l = [[int(d) for d in x.split()] for x in open('4.txt')]
for x in l:
    # 5, 5, 4, 4, 1, 2, 3 +
    # 5, 5, 5, 1, 2, 3, 4 -
    if x.count(max(x)) == 1:
        povt = []
        nepovt = []
        for y in x:
            if x.count(y) == 1:
                nepovt.append(y)
            if x.count(y) == 2:
                povt.append(y)
        if len(nepovt) == 3 and len(povt) == 4:
            print(sum(x))