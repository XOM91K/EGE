import itertools
otv = []
ct = 0
for x in set(itertools.permutations('ПРОСТО', 6)):
    x = ''.join(x)
    if 'ПП' not in x and 'РР' not in x and 'ОО' not in x and 'СС' not in x and 'ТТ' not in x:
        ct += 1
print(ct)