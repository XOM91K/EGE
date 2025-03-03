import itertools
s = set()
def F(x, y, z, w):
    return (w or y) and (x <= (not z)) and (not w)
for i in itertools.product([0, 1], repeat=5):
    table = [(i[0], 0, i[1], 0),
             (1, i[2], i[3], i[4]),
             (1, 1, 0, 0)]
    if len(set(table)) == len(table):
        for j in itertools.permutations('xyzw'):
            if [F(**dict(zip(j, r))) for r in table] == [1, 1, 1]:
                s.add(j)
print(len(s))
# l = [x for x in range(1, 1000_000)]
# t = (x for x in range(1, 1000_000))
# s = {1, 2, 3}
# print(l.__sizeof__()) #dunder-методы
# print(t.__sizeof__())