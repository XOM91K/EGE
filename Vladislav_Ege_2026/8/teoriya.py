import itertools
# iteration tools
#permutations - перестановки
# for x in itertools.permutations('ГОРА'):
#     x = ''.join(x)
#     if 'ГО' not in x:
#         print(x)

for x in itertools.product('ГОРА', repeat=4):
    x = ''.join(x)
    print(x)