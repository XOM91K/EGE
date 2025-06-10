import itertools
ct = 0
for x in itertools.product('ЕИЙКНОТ', repeat=7):
    x = ''.join(x)
    if 'КОТ' in x:
        ct += 1
print(ct)