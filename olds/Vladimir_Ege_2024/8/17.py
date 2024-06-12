import itertools
ct = 0
for x in itertools.product('012345678', repeat=7):
    if x[0] not in '026' and x[-1] != x[-2]:
        ct += 1
print(ct)