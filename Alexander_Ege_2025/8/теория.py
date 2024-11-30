import itertools
ct = 0
for x in itertools.product('9702', repeat=4):
    x = ''.join(x)
    print(x)
    ct += 1
print(ct)
ct2 = 0
print('----------------')
for x in itertools.permutations('9702', 4):
    x = ''.join(x)
    print(x)
    ct2 += 1
print(ct2)