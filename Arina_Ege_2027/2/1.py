import itertools
def F(x, y, z, w):
    return x or z and (y <= (w and (not z)))
ct = 0
for i in itertools.product([0, 1], repeat=11):
    table = [(i[0], 0, 1, 0),
             (i[1], i[2], i[3], 1),
             (i[4], i[5], 1, i[6]),
             (i[7], i[8], 1, i[9]),
             (i[10], 1, 1, 1)]
    if len(set(table)) == 5:
        for j in itertools.permutations('xyzw'):
            if [F(**dict(zip(j, r))) for r in table] == [0, 0, 0, 0, 0]:
                print(j)
# print(dict(zip('xwzy', (1, 0, 1, 0))))
# s = 'abracadabra'
# print(len(set(s)))