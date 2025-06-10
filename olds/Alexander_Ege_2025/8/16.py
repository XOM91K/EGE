import itertools
ct = 0
for x in itertools.product('НИКОЛАЙ', repeat=4):
    x = ''.join(x)
    if x[0] != 'Й' and ('И' in x or 'А' in x or 'О' in x):
        ct += 1
print(ct)