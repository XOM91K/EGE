import itertools
ct = 0
for x in set(itertools.permutations('МРАМОР', 6)):
    x = ''.join(x)
    if 'ММ' not in x and 'РР' not in x:
        ct += 1
print(ct)