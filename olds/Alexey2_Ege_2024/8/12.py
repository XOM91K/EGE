import itertools
ct = 0
for x in itertools.permutations('014689acefg', 6):
    x = ''.join(x)
    if x[0] != '0' and x[0] not in '19f':
        ct += 1
print(ct)