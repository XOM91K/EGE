l = [[int(d) for d in x.split()] for x in open('11.txt')]
k = 0
for x in l:
    k += 1
    if sorted(x) == x:
        can = -1
        for y in x:
            if x.count(y) > 1 and sum(map(int, str(y))) % 2 != 0:
                can = 0
                break
            elif x.count(y) > 1 and sum(map(int, str(y))) % 2 == 0:
                can = 1
        if can == 1:
            print(k, x)