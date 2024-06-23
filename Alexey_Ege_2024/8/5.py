import itertools
ct = 0
for x in itertools.product('КОМПЕГЭ', repeat=6):
    x = ''.join(x)
    if x[0] not in 'КМПГ' and x[5] not in 'КМПГ' and x[1] not in 'ОЕЭ' and x[2] not in 'ОЕЭ' and x[3] not in 'ОЕЭ' and x[4] not in 'ОЕЭ':
        ct += 1
print(ct)