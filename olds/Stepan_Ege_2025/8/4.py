import itertools
ct = 0
for x in itertools.product('КОМПЕГЭ', repeat=6):
    x = ''.join(x)
    if x[0] in 'ОЕЭ' and x[-1] in 'ОЕЭ':
        if x[1] in 'КМПГ' and x[2] in 'КМПГ' and x[3] in 'КМПГ' and x[4] in 'КМПГ':
            ct += 1
print(ct)