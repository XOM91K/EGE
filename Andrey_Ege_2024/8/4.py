import itertools
ct = 0
for x in itertools.permutations('ТИМАШЕВСК'):
    x = ''.join(x)
    sg = 'ТМШВСК'
    gl = 'ИАЕ'
    if x[0] in sg and x[-1] in sg:
        if ('ИАЕ' in x) or ('ИЕА' in x) or ('АИЕ' in x) or ('АЕИ' in x) or ('ЕИА' in x) or ('ЕАИ' in x):
            ct += 1
print(ct)