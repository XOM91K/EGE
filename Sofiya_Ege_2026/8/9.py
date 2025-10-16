import itertools
# 0 - 15  15_5
# 0 2 4 6 8 10 12 14  8_3
ct = 0
for x in set(itertools.permutations('xxxxxччч')):
    if x[0] == 'ч':
        ct += 8 ** 7 * 7
    else:
        ct += 8 ** 8
print(ct)