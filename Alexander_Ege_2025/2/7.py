import itertools
def F(x, y, z, w):
    return ((z <= w) <= (not y)) and x
# for i in itertools.product([0, 1], repeat=5):
#     table = [(0, 0, 1, i[0]),
#              (i[1], i[2], 0, i[3]),
#              (0, i[4], 1, 1)]
#     if len(set(table)) == len(table):
#         for j in itertools.permutations('xyzw'):
#             if [F(**dict(zip(j, r))) for r in table] == [1, 1, 0]:
#                 print(j)
#print(dict(zip('wzyx', (1, 0, 0, 1))))