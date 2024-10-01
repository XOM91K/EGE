from itertools import permutations
ct = 0
letters = 'ГЛУБИНА'
for p in permutations(letters, 7):
    p = ''.join(p)
    if (p.find('А') < p.find('И') < p.find('Г')) \
        or (p.find('И') < p.find('А') < p.find('Г')):
        ct += 1
print(ct)