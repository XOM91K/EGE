k = 0
import itertools
for x in itertools.permutations('014689ACEFG', 6):
    x = ''.join(x)
    if x[0] != '0' and x[0] in '468ACEG':
        k += 1
print(k)