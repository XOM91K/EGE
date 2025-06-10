l = [[int(d) for d in x.split()] for x in open('4.txt')]
compains = [0, 0, 0, 0]
for x in range(4):
    for i in range(len(l)):
        mn = 10 ** 5
        for k in range(len(l)):
            for j in range(4):
                mn = min(mn, l[k][j])
            for i in range(len(l)):
                if mn == l[i][j]:
                    if compains[x] + mn <= 200:
                        compains[x] += mn
                        del l[i][j]
                    break

for x in l:
    print(x)