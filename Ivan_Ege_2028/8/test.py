import itertools
# iteration tools
# for x in itertools.permutations('СЛОН', r=4):
#     print(x)
# 4*4*4*4  4**4
for x in itertools.product('СЛОН', repeat=4):
    print(x)