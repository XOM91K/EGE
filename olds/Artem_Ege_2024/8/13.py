import itertools
k = 0
ct = 0
for x in itertools.product('АЕЖЙМУ', repeat=5):
    x = ''.join(x)
    k += 1
    if k % 2 == 0:
        if 'АА' not in x and 'ЕЕ' not in x and 'ЖЖ' not in x and 'ЙЙ' not in x and 'ММ' not in x and 'УУ' not in x:
            ct += 1
print(ct)