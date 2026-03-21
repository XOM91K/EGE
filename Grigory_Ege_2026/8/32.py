import itertools, tqdm
ct = 0
for x in itertools.product('123456789ABCDEF', repeat=6):
    x = ''.join(x)
    for l in 'ABCDEF':
        x = x.replace(l, '*')
    if x.count('*') <= 4:
        ct += 1
print(ct)
print(10924065 * 21)