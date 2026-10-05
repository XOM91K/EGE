l = [[int(d) for d in x.split()] for x in open('18.txt')]
k = 0
for x in l:
    k += 1
    # 7 14 21 50 50 # неубывание <=
    # 7 14 21 50 51 # возрастание <
    if x[0] <= x[1] <= x[2] <= x[3] <= x[4]:
        povt = [y for y in x if x.count(y) >= 2 and sum(map(int, str(y))) % 2 == 0]
        if len(povt) > 0:
            print(k, x, povt)