import itertools
ct = 0
for x in itertools.permutations('ВУАЛЬ'):
    x = ''.join(x)
    if x[0] != 'Ь' and 'ЬУ' not in x and 'ЬА' not in x:
        ct += 1
print(ct)