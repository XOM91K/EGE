l = [[int(y) for y in x.split()] for x in open('12.txt')]
k = 0
for x in l:
    k += 1
    if sorted(x) == x:
        can = False
        for y in x:
            if x.count(y) > 1 and sum(map(int, str(y))) % 2 == 0:
                can = True
                break
        if can:
            print(k)