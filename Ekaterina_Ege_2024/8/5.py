import itertools
ct = 0
for x in itertools.product("ТИМОФЕЙ", repeat=6):
    x = ''.join(x)
    x = x.replace('И', 'А')
    x = x.replace('О', 'А')
    x = x.replace('Е', 'А')
    x = x.replace('Т', 'М')
    x = x.replace('Ф', 'М')
    x = x.replace('Й', 'М')
    if x.count('А') == x.count('М'):
        ct += 1
print(ct)