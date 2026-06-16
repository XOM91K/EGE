2 5 16 13
import itertools
for x in itertools.permutations('МЕД'):
    x = ''.join(x)
    print(x)
print('------------')
for x in itertools.product('МЕД', repeat=3):
    x = ''.join(x)
    print(x)