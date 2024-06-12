import itertools
def f(x, y, z, w):
    return ((x <= y) or w) == (z <= (x and y))
st = set()
for i in itertools.product([0, 1], repeat=3):
    table = [(i[0], 0, 1, 0), (0, i[1], 1, 1), (0, 0, i[2], 1)]
    if len(table) == len(set(table)):
        for j in itertools.permutations('xzw'):
            if [f(**dict(zip(('y',) + j, r))) for r in table] == [0, 0, 0]:
                st.add(j)
print(st)