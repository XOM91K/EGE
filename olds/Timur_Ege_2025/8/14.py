import itertools
ct = 0
for x in itertools.product('ИГОРЬ', repeat = 8):
    x = ''.join(x)
    if x[0] != 'Ь':
        if x.count('О') == 1 and x.count('Ь') == 1:
            ct += 1
            #ОГГГЬ
            #ГОРРЬ
print(ct)