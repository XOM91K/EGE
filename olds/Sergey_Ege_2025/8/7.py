import itertools
k = 0
for x in itertools.permutations('АЛНРСУ', 6):
    x = ''.join(x)
    k += 1
    if k == 442:
        print(x)
        break