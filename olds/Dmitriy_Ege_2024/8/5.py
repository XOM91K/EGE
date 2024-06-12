import itertools
ct = 0
for x in itertools.permutations('тимашевск'):
    x = ''.join(x)
    x = x.replace('и', 'а')
    x = x.replace('е', 'а')
    x = x.replace('м', 'т')
    x = x.replace('ш', 'т')
    x = x.replace('в', 'т')
    x = x.replace('с', 'т')
    x = x.replace('к', 'т')
    if 'ааа' in x and x[0] == x[-1] == 'т':
        ct += 1
print(ct)