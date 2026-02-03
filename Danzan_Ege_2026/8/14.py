import itertools
d = [''.join(d) for d in list(itertools.product(sorted('АИКЛМЬ'), repeat=6))]
for x in range(len(d) - 26655):
    if d[x][0] == 'К' and d[x][-1] == 'Ь' and d[x + 26655][::-1] == d[x] and len(set(d[x])) == 6:
        print(x + 1, d[x])
# for x in itertools.permutations(sorted('АИКЛМЬ'), 6):
#     x = ''.join(x)
#     k += 1
#     if x[0] == 'К' and x[-1] == 'Ь':
#         print(k, x)
