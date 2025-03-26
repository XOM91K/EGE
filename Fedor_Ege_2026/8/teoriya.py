import itertools
# iteration tools
# 4! = 1 * 2 * 3 * 4 = 24
# for x in itertools.permutations('слон', 4):
#     x = ''.join(x)
#     print(x)
# 4 ** 3 =
# for x in itertools.product('слон', 'слон', 'слон', 'слон', 'слон', 'слон'):
#     x = ''.join(x)
#     print(x)
for x in itertools.product('слон', repeat=5):
    x = ''.join(x)
    print(x)