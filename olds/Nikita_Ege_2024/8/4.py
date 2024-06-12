import itertools
ct = 0
for x in itertools.permutations('014689acefg', 6):
    x = ''.join(x)
    if x[0] in '468aceg':
        ct += 1
print(ct)