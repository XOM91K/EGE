import itertools
# iteration tools
for x in itertools.permutations('СЛОН', r=4):
    x = ''.join(x)
    print(x)
print('-------')
for x in itertools.product('СЛОН', repeat=3):
    x = ''.join(x)
    print(x)