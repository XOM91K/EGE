l = [[int(d) for d in x.split()] for x in open('19.txt')]
k = 0
for x in l:
    k += 1
    if sorted(x) == x:
        c = []
        for y in x:
            if x.count(y) > 1 and sum(map(int, str(y))) % 2 == 0:
                c.append(k)
print(max(c))