from itertools import product
ct = 0
letters = '012345'
for p in product(letters, repeat=3):
    p = ''.join(p)
    if p.count('5') == 1 and p[0] != '0':
        p = p.replace('2', '0')
        p = p.replace('4', '0')
        if '50' not in p and '05' not in p:
            ct += 1
print(ct)