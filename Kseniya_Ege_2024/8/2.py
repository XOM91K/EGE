import itertools
ct = 0
for x in itertools.permutations("СПОРТЛОТО"):
    x = ''.join(x)
    if 'ОО' in x:
        ct += 1
print(ct // 6 // 2)