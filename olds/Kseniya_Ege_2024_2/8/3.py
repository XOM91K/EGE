import itertools
ct = 0
for x in itertools.permutations("СПОРТЛОТО"):
    x = ''.join(x)
    print(x)