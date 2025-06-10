l = [[int(d) for d in x.split()] for x in open('11.txt')]
l = sorted(l, key=lambda x: (-(sum(x[1:]) / 4), x[0]))
l = sorted(l, key=lambda x: x[1:].count(2))
print(l[len(l) // 4 - 1][0])
for x in l:
    if x[1:].count(2) > 2:
        print(x[0])
        break