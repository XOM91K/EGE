import itertools
ct = 0
for x in set(itertools.permutations("СПОРТЛОТО")):
    x = ''.join(x)
    if 'ООО' in x:
        ct += 1
print(ct)