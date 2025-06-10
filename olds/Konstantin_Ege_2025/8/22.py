import itertools
ct = 0
for x in itertools.permutations('ТИМАШЕВСК'):
    x = ''.join(x)
    if x[0] in 'ТМШВСК' and x[-1] in 'ТМШВСК':
        x = x.replace('И', 'А')
        x = x.replace('Е', 'А')
        if 'ААА' in x:
            ct += 1
print(ct)