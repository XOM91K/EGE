import itertools
ct = 0
for x in itertools.permutations('ЛЕВИЙ', 5):
    x = ''.join(x)
    if x[0] != 'Й' and x.count('ЕИ') == 0:
        ct += 1
        print(x)
print(ct)