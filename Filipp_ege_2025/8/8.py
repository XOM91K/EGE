from itertools import product
ct = 0
letters = 'КРЕМНИЙ'
for p in product(letters, repeat=5):
    p = ''.join(p)
    if p.count('Е') + p.count('И') != 0 and (p.count('Е') + p.count('И')) % 2 == 0:
        if p.count('Й') <= 2:
            ct += 1
print(ct)