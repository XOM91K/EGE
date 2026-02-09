import itertools
k = 0
d = []
for x in itertools.product(sorted('АИКЛМЬ'), repeat=6):
    x = ''.join(x)
    k += 1
    if x[0] == 'К' and x[-1] == 'Ь' and len(set(x)) == 6:
        d.append([k, x])
g = list(itertools.product(sorted('АИКЛМЬ'), repeat=6))
g = [''.join(x) for x in g]
for x in range(len(g)):
    for y in d:
        if abs(x - y[0]) == 26655 and y[1] == g[x][::-1]:
            print(g[x], y)