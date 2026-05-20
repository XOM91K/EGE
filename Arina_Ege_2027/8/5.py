import itertools
ct = 0
for x in itertools.permutations('ЛЕВИЙ', 5):
    x = ''.join(x)
    if x[0] != 'Й' and 'ЕИ' not in x:
        ct += 1
print(ct)