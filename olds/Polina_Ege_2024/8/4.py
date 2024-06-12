import itertools
ct = 0
for x in itertools.permutations('0123456789abcdef', 5):
    x = ''.join(x)
    can = True
    for y in range(len(x) - 1):
        if (x[y] in '02468ace' and x[y + 1] in '2468ace') or (x[y] not in '02468ace' and x[y + 1] not in '2468ace'):
            can = False
    if can == True and x[0] != '0':
        print(x)
        ct += 1
print(ct)